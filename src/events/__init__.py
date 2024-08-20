from events.active_event import *
from events.audio_device_event import *
from events.clipboard_update_event import *
from events.controller_device_event import *
from events.drop_file_event import *
from events.drop_status_event import *
from events.drop_text_event import *
from events.event_type import *
from events.finger_event import *
from events.joy_axis_motion_event import *
from events.joy_ball_motion_event import *
from events.joy_button_event import *
from events.joy_device_event import *
from events.joy_hat_motion_event import *
from events.key_event import *
from events.keymap_changed_event import *
from events.locale_changed_event import *
from events.midi_event import *
from events.mouse_button_event import *
from events.mouse_motion_event import *
from events.mouse_wheel_event import *
from events.multi_gesture_event import *
from events.quit_event import *
from events.render_device_reset_event import *
from events.render_targets_reset_event import *
from events.text_editing_event import *
from events.text_input_event import *
from events.user_event import *
from events.video_expose_event import *
from events.video_resize_event import *
from events.window_close_event import *
from events.window_display_changed_event import *
from events.window_enter_event import *
from events.window_exposed_event import *
from events.window_focus_gained_event import *
from events.window_focus_lost_event import *
from events.window_hidden_event import *
from events.window_hit_test_event import *
from events.window_icc_profile_changed_event import *
from events.window_leave_event import *
from events.window_maximized_event import *
from events.window_minimized_event import *
from events.window_moved_event import *
from events.window_resized_event import *
from events.window_restored_event import *
from events.window_shown_event import *
from events.window_size_changed_event import *
from events.window_take_focus_event import *

type Event = (ActiveEvent
              | AudioDeviceEvent
              | ClipboardUpdateEvent
              | ControllerDeviceEvent
              | DropFileEvent
              | DropStatusEvent
              | DropTextEvent
              | FingerEvent
              | JoyAxisMotionEvent
              | JoyBallMotionEvent
              | JoyButtonEvent
              | JoyDeviceEvent
              | JoyHatMotionEvent
              | KeymapChangedEvent
              | KeyEvent
              | LocaleChangedEvent
              | MidiEvent
              | MouseButtonEvent
              | MouseMotionEvent
              | MouseWheelEvent
              | MultiGestureEvent
              | QuitEvent
              | RenderDeviceResetEvent
              | RenderTargetsResetEvent
              | TextEditingEvent
              | TextInputEvent
              | UserEvent
              | VideoExposeEvent
              | VideoResizeEvent
              | WindowCloseEvent
              | WindowDisplayChangedEvent
              | WindowEnterEvent
              | WindowExposedEvent
              | WindowFocusGainedEvent
              | WindowFocusLostEvent
              | WindowHiddenEvent
              | WindowHitTestEvent
              | WindowIccProfileChangedEvent
              | WindowLeaveEvent
              | WindowMaximizedEvent
              | WindowMinimizedEvent
              | WindowMovedEvent
              | WindowResizedEvent
              | WindowRestoredEvent
              | WindowShownEvent
              | WindowSizeChangedEvent
              | WindowTakeFocusEvent)
