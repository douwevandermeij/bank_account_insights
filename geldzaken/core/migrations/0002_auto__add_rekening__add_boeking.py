# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Rekening'
        db.create_table('core_rekening', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nr', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('naam_omschrijving', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('core', ['Rekening'])

        # Adding model 'Boeking'
        db.create_table('core_boeking', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('datum', self.gf('django.db.models.fields.DateField')()),
            ('tegenrekening', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Rekening'])),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('af', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('bedrag', self.gf('django.db.models.fields.FloatField')()),
            ('mutatiesoort', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('mededelingen', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('core', ['Boeking'])


    def backwards(self, orm):
        # Deleting model 'Rekening'
        db.delete_table('core_rekening')

        # Deleting model 'Boeking'
        db.delete_table('core_boeking')


    models = {
        'core.boeking': {
            'Meta': {'object_name': 'Boeking'},
            'af': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'bedrag': ('django.db.models.fields.FloatField', [], {}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'datum': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mededelingen': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'mutatiesoort': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'tegenrekening': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Rekening']"})
        },
        'core.rekening': {
            'Meta': {'object_name': 'Rekening'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam_omschrijving': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nr': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['core']