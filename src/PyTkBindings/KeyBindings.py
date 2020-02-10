import json


__all__ = ['Bindings']

class _base_(object):
    def __ToList__(self):
        l = []
        for name in dir(self):
            if name == 'ToJson' or name.startswith('_') or callable(name): continue
            value = getattr(self, name)
            if hasattr(value, '__ToList__'):
                value = value.__ToList__()

            elif isinstance(value, bytes):
                value = value.decode()

            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, bytes):
                        value = item.decode()
                    else:
                        value = item

            l.append(value)
        return l
    def __ToDict__(self):
        d = { }
        for name in dir(self):
            if name == 'ToJson' or name.startswith('_') or callable(name): continue
            value = getattr(self, name)
            if hasattr(value, '__ToDict__'):
                value = value.__ToDict__()

            elif isinstance(value, bytes):
                value = value.decode()

            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, bytes):
                        value = item.decode()
                    else:
                        value = item

            d[name] = value
        return d
    def __setattr__(self, key, value):
        if not hasattr(self, key):
            super().__setattr__(key, value)
    def __setitem__(self, key, value):
        if not hasattr(self, key):
            super().__setattr__(key, value)
    def ToJson(self):
        return json.dumps(self.__ToDict__(), sort_keys=True, indent=4)


class Core_Bindings_MixIn(_base_):
    Key = '<Key>'

    Cancel = 'Cancel'
    Shift_L = 'Shift_L'
    Control_L = 'Control_L'
    Alt_L = 'Alt_L'
    Pause = 'Pause'
    Caps_Lock = 'Caps_Lock'
    Escape = 'Escape'
    Prior = 'Prior'
    Next = 'Next'
    End = 'End'
    Home = 'Home'
    Left = 'Left'
    Up = 'Up'
    Right = 'Right'
    Down = 'Down'
    Print = 'Print'
    Insert = 'Insert'
    Num_Lock = 'Num_Lock'

    Shift = 'Shift'
    Tab = 'Tab'

    Scroll_Lock = 'Scroll_Lock'
    KP_Enter = 'KP_Enter'
    KP_Subtract = 'KP_Subtract'
    KP_Add = 'KP_Add'

    BackSpace = 'BackSpace'
    Delete = 'Delete'

    Minus = 'minus'
    Plus = 'plus'

    Enter = 'Enter'
    Return = 'Return'  # the Enter key

    Shift_Up = '<Shift-Up>'
    Shift_Down = '<Shift-Down>'
    Shift_Right = '<Shift-Right>'
    Shift_Left = '<Shift-Left>'

    FocusIn = '<FocusIn>'
    FocusOut = '<FocusOut>'
    Enter_Boundary = '<Enter>'
    Leave_Boundary = '<Leave>'

class Special_Bindings_MixIn(_base_):
    Configure = '<Configure>'
    Activate = '<Activate>'
    Deactivate = '<Deactivate>'
    Destroy = '<Destroy>'
    Expose = '<Expose>'
    Map = "<Map>"
    Unmap = '<Unmap>'
    Motion = '<Motion>'
    MouseWheel = '<MouseWheel>'
    Visibility = '<Visibility>'

class Numbers_Bindings_MixIn(_base_):
    zero = '0'
    one = '1'
    two = '2'
    three = '3'
    four = '4'
    five = '5'
    six = '6'
    seven = '7'
    eight = '8'
    nine = '9'

class FunctionKey_Bindings_MixIn(_base_):
    bindF1 = '<F1>'
    F1 = 'F1'
    bindF2 = '<F2>'
    F2 = 'F2'
    bindF3 = '<F3>'
    F3 = 'F3'
    bindF4 = '<F4>'
    F4 = 'F4'
    bindF5 = '<F5>'
    F5 = 'F5'
    bindF6 = '<F6>'
    F6 = 'F6'
    bindF7 = '<F7>'
    F7 = 'F7'
    bindF8 = '<F8>'
    F8 = 'F8'
    bindF9 = '<F9>'
    F9 = 'F9'
    bindF10 = '<F10>'
    F10 = 'F10'
    bindF11 = '<F11>'
    F11 = 'F11'
    bindF12 = '<F12>'
    F12 = 'F12'

class Letters_Bindings_MixIn(_base_):
    a = 'a'
    b = 'b'
    c = 'c'
    d = 'd'
    e = 'e'
    f = 'f'
    g = 'g'
    h = 'h'
    i = 'i'
    j = 'j'
    k = 'k'
    l = 'l'
    m = 'm'
    n = 'n'
    o = 'o'
    p = 'p'
    q = 'q'
    r = 'r'
    s = 's'
    t = 't'
    u = 'u'
    v = 'v'
    w = 'w'
    x = 'x'
    y = 'y'
    z = 'z'
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    E = 'E'
    F = 'F'
    G = 'G'
    H = 'H'
    I = 'I'
    J = 'J'
    K = 'K'
    L = 'L'
    M = 'M'
    N = 'N'
    O = 'O'
    P = 'P'
    Q = 'Q'
    R = 'R'
    S = 'S'
    T = 'T'
    U = 'U'
    V = 'V'
    W = 'W'
    X = 'X'
    Y = 'Y'
    Z = 'Z'

class Mouse_Bindings_MixIn(_base_):
    Button = "<Button>"
    Button1 = "<Button1>"
    Button2 = "<Button2>"
    Button3 = "<Button3>"

    B1_Motion = '<B1-Motion>'
    B2_Motion = '<B2-Motion>'

    ButtonRelease = '<ButtonRelease>'
    ButtonRelease1 = '<ButtonRelease-1>'
    ButtonRelease2 = '<ButtonRelease-2>'
    ButtonRelease3 = '<ButtonRelease-3>'

    Double_Button = '<Double-Button>'
    Double_Button2 = '<Double-Button-2>'
    Double_Button3 = '<Double-Button-3>'

class ListBox_Bindings_MixIn(_base_):
    ListboxSelect = "<<ListboxSelect>>"

class TreeView_Bindings_MixIn(_base_):
    TreeViewSelect = "<<TreeviewSelect>>"

class Custom_Bindings_MixIn(_base_):
    ShiftTab = 'ShiftTab'
    ShiftTabEvent = '<Shift-KeyPress-Tab>'
class Other_Bindings_MixIn(_base_):
    pass


class All_Key_Bindings(_base_):
    """
        Made with help from:
            https://stackoverflow.com/a/32289245/9530917
            https://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
            https://www.tcl.tk/man/tcl8.4/TkCmd/keysyms.htm


<Button-1>        Button 1 is the leftmost button, button 2 is the middle button
                  (where available), and button 3 the rightmost button.

                  <Button-1>, <ButtonPress-1>, and <1> are all synonyms.

                  For mouse wheel support under Linux, use Button-4 (scroll
                  up) and Button-5 (scroll down)

<B1-Motion>       The mouse is moved, with mouse button 1 being held down (use
                  B2 for the middle button, B3 for the right button).

<ButtonRelease-1> Button 1 was released. This is probably a better choice in
                  most cases than the Button event, because if the user
                  accidentally presses the button, they can move the mouse
                  off the widget to avoid setting off the event.

<Double-Button-1> Button 1 was double clicked. You can use Double or Triple as
                  prefixes.

<Enter>           The mouse pointer entered the widget (this event doesn’t mean
                  that the user pressed the Enter key!).

<Leave>           The mouse pointer left the widget.

<FocusIn>         Keyboard focus was moved to this widget, or to a child of
                  this widget.

<FocusOut>        Keyboard focus was moved from this widget to another widget.

<Return>          The user pressed the Enter key. For an ordinary 102-key
                  PC-style keyboard, the special keys are Cancel (the Break
                  key), BackSpace, Tab, Return(the Enter key), Shift_L (any
                  Shift key), Control_L (any Control key), Alt_L (any Alt key),
                  Pause, Caps_Lock, Escape, Prior (Page Up), Next (Page Down),
                  End, Home, Left, Up, Right, Down, Print, Insert, Delete, F1,
                  F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12, Num_Lock, and
                  Scroll_Lock.

<Key>             The user pressed any key. The key is provided in the char
                  member of the event object passed to the callback (this is an
                  empty string for special keys).

a                 The user typed an “a”. Most printable characters can be used
                  as is. The exceptions are space (<space>) and less than
                  (<less>). Note that 1 is a keyboard binding, while <1> is a
                  button binding.

<Shift-Up>        The user pressed the Up arrow, while holding the Shift key
                  pressed. You can use prefixes like Alt, Shift, and Control.

<Configure>       The widget changed size (or location, on some platforms). The
                  new size is provided in the width and height attributes of
                  the event object passed to the callback.

<Activate>        A widget is changing from being inactive to being active.
                  This refers to changes in the state option of a widget such
                  as a button changing from inactive (grayed out) to active.


<Deactivate>      A widget is changing from being active to being inactive.
                  This refers to changes in the state option of a widget such
                  as a radiobutton changing from active to inactive (grayed out).

<Destroy>         A widget is being destroyed.

<Expose>          This event occurs whenever at least some part of your
                  application or widget becomes visible after having been
                  covered up by another window.

<KeyRelease>      The user let up on a key.

<Map>             A widget is being mapped, that is, made visible in the
                  application. This will happen, for example, when you call the
                  widget's .grid() method.

<Motion>          The user moved the mouse pointer entirely within a widget.

<MouseWheel>      The user moved the mouse wheel up or down. At present, this
                  binding works on Windows and MacOS, but not under Linux. (as of 8/28/2015; untested today)

<Unmap>           A widget is being unmapped and is no longer visible.

<Visibility>      Happens when at least some part of the application window
                  becomes visible on the screen.


    """
    core = Core_Bindings_MixIn()
    special = Special_Bindings_MixIn()
    numbers = Numbers_Bindings_MixIn()
    functionKeys = FunctionKey_Bindings_MixIn()
    letters = Letters_Bindings_MixIn()
    custom = Custom_Bindings_MixIn()
    mouse = Mouse_Bindings_MixIn()
    listBox = ListBox_Bindings_MixIn()
    treeView = TreeView_Bindings_MixIn()


    def __isEnter__(self, keysym: str) -> bool:
        return keysym == self.core.Enter or keysym == self.core.KP_Enter or keysym == self.core.Return


Bindings = All_Key_Bindings()


if __name__ == '__main__':
    d = Bindings.ToJson()
    print(d)



