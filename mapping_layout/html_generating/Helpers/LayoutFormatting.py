# body Styles
def BodyStyles():
    bStyles = 'style=\"margin:20px;background-color: #e6ffff;background-image: url(../bg-image.jpg);background-size: cover\"'
    return bStyles


# CSS, Script
def CSS_Scripts():
    links = '<title>Sample Web Page</title>\n<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">\n<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>\n<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>\n<link rel="stylesheet" href="Styles/Styles.css">'
    return links


# if tag is "label" - then enter <br> tag
# def br_tag(tag):
#     if (tag == "button") or (tag == "textarea") or (tag == "submit"):
#         br = "<br><br>"
#         return br
#     elif (tag == "radio") or (tag == "checkbox"):
#         return "<br>"
#     else:
#         return ""


# add attributes to tags(class)
def addClass(tag):
    if (tag == "submit"):
        return "class=\"btn btn-success text-capitalize\""
    elif (tag == "reset"):
        return "class=\"btn btn-danger text-capitalize\""
    if (tag == "button"):
        return "class=\"btn btn-secondary text-capitalize\""
    elif (tag == "a"):
        return "class=\"nav-link text-capitalize\""
    elif (tag == "dropdown"):
        return "class=\"btn btn-info dropdown-toggle form-control text-capitalize\""
    elif (tag == "img"):
        return "class=\"img-fluid\" src=\"../test.jpg\""
    elif (tag == "p"):
        return "class =\"text-justify text-dark\""
    elif (tag == "text") or (tag == "password") or (tag == "textarea"):
        return "class =\"form-control\""
    elif (tag == "label"):
        return "class =\"form-check-label text-capitalize\""
    elif (tag == "checkbox"):
        return "class =\"form-check-input text-capitalize\""
    elif (tag == "radio"):
        return "class =\"form-check-input text-capitalize\""
    elif (tag == "h1" or tag == "h2" or tag == "h3" or tag == "h4" or tag == "h5" or tag == "h6"):
        return "class =\"text-dark\""
    else:
        return ""
