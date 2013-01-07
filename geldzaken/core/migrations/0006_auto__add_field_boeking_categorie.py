# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Boeking.categorie'
        db.add_column('core_boeking', 'categorie',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Categorie'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Boeking.categorie'
        db.delete_column('core_boeking', 'categorie_id')


    models = {
        'core.boeking': {
            'Meta': {'object_name': 'Boeking'},
            'af': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'bedrag': ('django.db.models.fields.FloatField', [], {}),
            'categorie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Categorie']", 'null': 'True', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'datum': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mededelingen': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'mutatiesoort': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'tegenrekening': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Rekening']"})
        },
        'core.categorie': {
            'Meta': {'object_name': 'Categorie'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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
            'categorie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Categorie']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam_omschrijving': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['core']