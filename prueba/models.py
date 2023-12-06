from odoo import models, fields

class botella(models.Model):
    _name = 'samu.botella'
    _description = 'samu.botella'
    capacidad = fields.Integer()
    color = fields.Char()
    precio = fields.Float()
    vendedor = fields.Many2one(comodel_name='samu.vendedores')


class vendedores(models.Model):
    _name = 'samu.vendedores'
    _description = 'samu.vendedores'
    name = fields.Char()
    apellido = fields.Char()
    botella = fields.One2many(comodel_name='samu.botella', inverse_name='vendedor', string='Botellas Relacionadas')

    #  Añade en una de las clases una función que calcule la media de una serie de valores enteros almacenados en los registros.
    def media(self):
        total = 0
        for botella in self.botella:
            total += botella.capacidad
        return total / len(self.botella)

    #  Cree una clase hija que herede funcionalidades y añada otras nuevas.

class vendedores2(models.Model):
    _name = 'samu.vendedores2'
    _description = 'samu.vendedores2'
    name = fields.Char()
    apellido = fields.Char()
    botella = fields.One2many(comodel_name='samu.botella', inverse_name='vendedor', string='Botellas Relacionadas')

    #  Añade en una de las clases una función que calcule la media de una serie de valores enteros almacenados en los registros.
    def media(self):
        total = 0
        for botella in self.botella:
            total += botella.capacidad
        return total / len(self.botella)



    

  