from ctpbee_webline.ext import model


class Admin(model.Model):
    id = model.Column(model.Integer, primary_key=True)
    username = model.Column(model.String(20))
    pwd = model.Column(model.String(20))
