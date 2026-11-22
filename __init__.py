# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Falling Leaves - Online Assets

Companion of the Falling Leaves extension (Blender Extensions version).
It downloads the optional leaf asset packs from the Hugging Face repository
into the user folder of Falling Leaves, where they show up in its Asset Panel
after the bundled assets. Its controls are drawn inside the Falling Leaves
Asset Panel and in these add-on preferences.

The internet is used only when the Download / Update button is clicked, and
only if 'Allow Online Access' is enabled in Blender.
"""

import bpy
import json
import os
import posixpath
import threading
import urllib.parse
import urllib.request

_MAIN_ID = 'falling_leaves'          # id of the Falling Leaves extension
_DOWNLOADED_DIR = 'downloaded'       # folder read by Falling Leaves
_HF_REPO = 'GBissieres/falling_leaves_assets'
_HF_API  = f'https://huggingface.co/api/datasets/{_HF_REPO}/tree/main/assets?recursive=true'
_HF_FILE = f'https://huggingface.co/datasets/{_HF_REPO}/resolve/main/'
_HF_PAGE = f'https://huggingface.co/datasets/{_HF_REPO}'
_MAIN_URL = 'https://extensions.blender.org/add-ons/falling-leaves/'
_IMG_EXT = ('.png', '.jpg', '.jpeg')

_dl = {'running': False, 'error': None, 'current': '', 'index': 0, 'count': 0,
       'done': 0, 'total': 0, 'new': 0}


# ---------------------------------------------------------------------------
# Falling Leaves location
# ---------------------------------------------------------------------------

def _main_package():
    """Package name of the enabled Falling Leaves add-on, or None."""
    keys = bpy.context.preferences.addons.keys()
    found = [k for k in keys if k == _MAIN_ID or k.endswith('.' + _MAIN_ID)]
    if not found:
        return None
    # prefer the Blender Extensions install when several copies exist
    found.sort(key=lambda k: (not k.startswith('bl_ext.blender_org.'), k))
    return found[0]


def _dest_dir(main_package, create=False):
    """The 'downloaded' user folder of Falling Leaves (survives its updates)."""
    if main_package and main_package.startswith('bl_ext.'):
        try:
            return bpy.utils.extension_path_user(main_package, path=_DOWNLOADED_DIR,
                                                 create=create)
        except Exception:
            pass
    try:   # same fallback as Falling Leaves itself (legacy add-on install)
        return bpy.utils.user_resource(
            'CONFIG', path=os.path.join('falling_leaves', _DOWNLOADED_DIR), create=create)
    except Exception:
        return None


def _downloaded_count(main_package):
    d = _dest_dir(main_package)
    if d and os.path.isdir(d):
        return len([f for f in os.listdir(d) if f.lower().endswith('.blend')])
    return 0


# ---------------------------------------------------------------------------
# Download (background thread)
# ---------------------------------------------------------------------------

def _http(url):
    return urllib.request.urlopen(
        urllib.request.Request(url, headers={'User-Agent': 'FallingLeaves-OnlineAssets'}),
        timeout=30)


def _download_worker(dest_dir):
    tmp = None
    try:
        os.makedirs(dest_dir, exist_ok=True)
        with _http(_HF_API) as r:
            tree = json.loads(r.read().decode('utf-8'))
        files = {e['path']: e for e in tree if e.get('type') == 'file'}
        wanted = []
        for path in sorted(files):
            low = path.lower()
            if '/menu_icons/' in low:         # old panel icons: not assets
                continue
            # the .blend packs + every image, also from sub-folders such as
            # assets/icons/ (the visuals of the assets)
            if low.endswith('.blend') or low.endswith(_IMG_EXT):
                wanted.append(path)
        if not any(p.lower().endswith('.blend') for p in wanted):
            raise IOError('No .blend asset found in the repository')
        _dl['count'] = len(wanted)
        for i, path in enumerate(wanted, 1):
            entry = files[path]
            size = (entry.get('lfs') or {}).get('size') or entry.get('size') or 0
            target = os.path.join(dest_dir, posixpath.basename(path))
            _dl.update(current=posixpath.basename(path), index=i, done=0, total=size)
            if size and os.path.isfile(target) and os.path.getsize(target) == size:
                continue                      # already up to date
            tmp = target + '.part'
            with _http(_HF_FILE + urllib.parse.quote(path)) as r, open(tmp, 'wb') as f:
                _dl['total'] = int(r.headers.get('Content-Length') or size or 0)
                while True:
                    chunk = r.read(1 << 20)
                    if not chunk:
                        break
                    f.write(chunk)
                    _dl['done'] += len(chunk)
            if _dl['total'] and os.path.getsize(tmp) != _dl['total']:
                raise IOError(f'Incomplete download: {path}')
            os.replace(tmp, target)
            tmp = None
            _dl['new'] += 1
    except Exception as e:
        _dl['error'] = str(e)
        if tmp and os.path.exists(tmp):
            try:
                os.remove(tmp)
            except OSError:
                pass
    finally:
        _dl['running'] = False


class FLONLINE_OT_DownloadAssets(bpy.types.Operator):
    bl_idname      = 'fl_online.download_assets'
    bl_label       = 'Download Online Assets'
    bl_description = ('Download or update the optional leaf assets (with their thumbnails) '
                      'from the Hugging Face repository. They are added to the Falling '
                      'Leaves Asset Panel, after the bundled ones')

    target_package: bpy.props.StringProperty(options={'HIDDEN', 'SKIP_SAVE'})

    _timer = None

    def execute(self, context):
        if _dl['running']:
            return {'CANCELLED'}
        if not getattr(bpy.app, 'online_access', True):
            self.report({'ERROR'}, "Enable 'Allow Online Access' in "
                                   "Preferences > System > Network")
            return {'CANCELLED'}
        pkg = self.target_package or _main_package()
        if not pkg:
            self.report({'ERROR'}, 'Install and enable Falling Leaves first '
                                   '(Blender Extensions).')
            return {'CANCELLED'}
        dest = _dest_dir(pkg, create=True)
        if not dest:
            self.report({'ERROR'}, 'Could not find the Falling Leaves user folder.')
            return {'CANCELLED'}
        _dl.update(running=True, error=None, current='', index=0, count=0,
                   done=0, total=0, new=0)
        threading.Thread(target=_download_worker, args=(dest,), daemon=True).start()
        wm = context.window_manager
        self._timer = wm.event_timer_add(0.5, window=context.window)
        wm.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    def modal(self, context, event):
        if event.type != 'TIMER':
            return {'PASS_THROUGH'}
        for win in context.window_manager.windows:
            for area in win.screen.areas:
                area.tag_redraw()
        if _dl['running']:
            return {'PASS_THROUGH'}
        context.window_manager.event_timer_remove(self._timer)
        if _dl['error']:
            self.report({'ERROR'}, f"Download failed: {_dl['error']}")
            return {'CANCELLED'}
        if _dl['new']:
            self.report({'INFO'}, f"{_dl['new']} file(s) downloaded: the assets are "
                                  "now in the Falling Leaves Asset Panel.")
        else:
            self.report({'INFO'}, 'Online assets are already up to date.')
        return {'FINISHED'}


# ---------------------------------------------------------------------------
# UI
# ---------------------------------------------------------------------------

def _draw_status(layout, main_package):
    """Progress while downloading, otherwise the Download / Update button."""
    if _dl['running']:
        mb = _dl['done'] / 1048576
        total = _dl['total'] / 1048576
        txt = f"Downloading {_dl['current']} ({_dl['index']}/{_dl['count']})"
        if total:
            txt += f": {mb:.0f} / {total:.0f} MB"
        layout.label(text=txt, icon='SORTTIME')
        return
    if _dl['error']:
        layout.label(text=f"Error: {_dl['error']}", icon='CANCEL')
    n = _downloaded_count(main_package)
    op = layout.operator('fl_online.download_assets',
                         text='Update Online Assets' if n else 'Download Online Assets',
                         icon='IMPORT')
    op.target_package = main_package or ''


def draw_asset_panel(layout, main_package):
    """Called by Falling Leaves to draw this section inside its Asset Panel."""
    n = _downloaded_count(main_package)
    layout.label(text=f"Online assets: {n} downloaded" if n else "Online assets (optional)",
                 icon='URL')
    _draw_status(layout, main_package)


class FLONLINE_Preferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    def draw(self, context):
        layout = self.layout
        pkg = _main_package()
        box = layout.box()
        if not pkg:
            box.label(text='Falling Leaves is not installed or not enabled.', icon='ERROR')
            box.label(text='Install it from Blender Extensions first, then come back here.')
            op = box.operator('wm.url_open', text='Falling Leaves on Blender Extensions',
                              icon='URL')
            op.url = _MAIN_URL
            return
        n = _downloaded_count(pkg)
        if n:
            box.label(text=f'{n} online asset pack(s) downloaded', icon='CHECKMARK')
        else:
            box.label(text='No online asset downloaded yet (the 3 bundled assets '
                           'always work)', icon='INFO')
        _draw_status(box, pkg)
        col = box.column(align=True)
        col.label(text='Connects to the internet only when you click the button.')
        col.label(text='New assets are added over time: click Update to get them.')
        row = box.row(align=True)
        d = _dest_dir(pkg)
        if d and os.path.isdir(d):
            op = row.operator('wm.path_open', text='Open Assets Folder', icon='FILE_FOLDER')
            op.filepath = d
        op = row.operator('wm.url_open', text='Asset Repository', icon='URL')
        op.url = _HF_PAGE


# ---------------------------------------------------------------------------
# Register
# ---------------------------------------------------------------------------

classes = (
    FLONLINE_OT_DownloadAssets,
    FLONLINE_Preferences,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
