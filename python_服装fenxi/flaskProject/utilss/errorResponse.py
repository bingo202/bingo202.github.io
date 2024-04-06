from flask import render_template

def errorResponse(errorMsg):
    return render_template('error-404.html',errorMsg=errorMsg)