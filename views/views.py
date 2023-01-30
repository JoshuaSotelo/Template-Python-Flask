from flask import Blueprint
from flask import render_template,url_for, Blueprint
from flask_login import current_user
from extensions import db
views = Blueprint('views', __name__)
#                                                   error handler´s functions
@views.errorhandler(404)
def page_not_found(e):
    pagina_css = url_for('static', filename='styles/404.css')
    return render_template("404.html", pagina_css=pagina_css, e=e), 404


@views.errorhandler(500)
def page_not_found(e):
    pagina_css = url_for('static', filename='styles/500.css')
    return render_template("500.html", e=e,  pagina_css=pagina_css, user=current_user), 500


@views.errorhandler(505)
def page_not_found(e):
    pagina_css = url_for('static', filename='styles/505.css')
    return render_template("505.html", e=e,  pagina_css=pagina_css, user=current_user), 505

@views.route('/eliminar-pedido-hecho/<int:id>')
def eliminar_pedido_hecho(id):
    print("Hola :)")
