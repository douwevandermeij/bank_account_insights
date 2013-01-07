# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'RawData.processed'
        db.add_column('core_rawdata', 'processed',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'RawData.processed'
        db.delete_column('core_rawdata', 'processed')


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
            'processed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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