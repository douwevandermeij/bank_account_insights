# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RawData'
        db.create_table('core_rawdata', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('datum', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('naam_omschrijving', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('rekening', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('tegenrekening', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('af_bij', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('bedrag', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('mutatiesoort', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('mededelingen', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('core', ['RawData'])


    def backwards(self, orm):
        # Deleting model 'RawData'
        db.delete_table('core_rawdata')


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
        'core.rawdata': {
            'Meta': {'object_name': 'RawData'},
            'af_bij': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'bedrag': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'datum': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mededelingen': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'mutatiesoort': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'naam_omschrijving': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'rekening': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'tegenrekening': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'core.rekening': {
            'Meta': {'object_name': 'Rekening'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam_omschrijving': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nr': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['core']