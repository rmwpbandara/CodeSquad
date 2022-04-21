# setup form when receive form elements -- form starting tag
def formSetUp(tag):
    if (tag == "input") or (tag == "radio") or (tag == "checkbox") or (tag == "reset") or (tag == "submit") or (
            tag == "textarea") or (tag == "text") or (tag == "password"):
        return "<div>\n<form class=\"form-inline\">"
    else:
        return ""


# form ending tag
def formSetDown(tag):
    if (tag == "input") or (tag == "radio") or (tag == "checkbox") or (tag == "reset") or (tag == "submit") or (
            tag == "textarea") or (tag == "text") or (tag == "password"):
        return "</form>\n</div>"
    else:
        return ""


# if input type=password set tag type=input // type=dropdown set tag type=select
def input_password(tag):
    if (tag == "password") or (tag == "radio") or (tag == "checkbox") or (tag == "text"):
        return "input"
    elif (tag == "submit") or (tag == "reset"):
        return "button"
    elif (tag == "dropdown"):
        return "select"
    else:
        return tag
