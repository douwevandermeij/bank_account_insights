# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CategorizeFilter'
        db.create_table('core_categorizefilter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('field', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('categorie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Categorie'])),
        ))
        db.send_create_signal('core', ['CategorizeFilter'])


        # Changing field 'Rekening.categorie'
        db.alter_column('core_rekening', 'categorie_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Categorie']))

    def backwards(self, orm):
        # Deleting model 'CategorizeFilter'
        db.delete_table('core_categorizefilter')


        # Changing field 'Rekening.categorie'
        db.alter_column('core_rekening', 'categorie_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Categorie'], null=True))

    models = {
        'core.boeking': {
            'Meta': {'object_name': 'Boeking'},
            'af': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'bedrag': ('django.db.models.fields.FloatField', [], {}),
            'categorie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Categorie']", 'null': 'True', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'datum': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mededelingen': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'mutatiesoort': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'tegenrekening': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Rekening']"})
        },
        'core.categorie': {
            'Meta': {'object_name': 'Categorie'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'core.categorizefilter': {
            'Meta': {'object_name': 'CategorizeFilter'},
            'categorie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Categorie']"}),
            'field': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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
            'categorie': ('django.db.models.fields.related.ForeignKey', [], {'default': '17', 'to': "orm['core.Categorie']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam_omschrijving': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['core']