# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Campaign.state'
        db.add_column(u'referral_campaign', 'state',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Campaign.created'
        db.add_column(u'referral_campaign', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2016, 3, 28, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Campaign.created_by'
        db.add_column(u'referral_campaign', 'created_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='campaign_created_by', to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'Campaign.updated'
        db.add_column(u'referral_campaign', 'updated',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2016, 3, 28, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Campaign.updated_by'
        db.add_column(u'referral_campaign', 'updated_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='campaign_updated_by', null=True, to=orm['auth.User']),
                      keep_default=False)

        # Deleting field 'Referrer.sender'
        db.delete_column(u'referral_referrer', 'sender_id')

        # Adding field 'Referrer.state'
        db.add_column(u'referral_referrer', 'state',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Referrer.created'
        db.add_column(u'referral_referrer', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2016, 3, 28, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Referrer.created_by'
        db.add_column(u'referral_referrer', 'created_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='referrer_created_by', to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'Referrer.updated'
        db.add_column(u'referral_referrer', 'updated',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2016, 3, 28, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Referrer.updated_by'
        db.add_column(u'referral_referrer', 'updated_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='referrer_updated_by', null=True, to=orm['auth.User']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Campaign.state'
        db.delete_column(u'referral_campaign', 'state')

        # Deleting field 'Campaign.created'
        db.delete_column(u'referral_campaign', 'created')

        # Deleting field 'Campaign.created_by'
        db.delete_column(u'referral_campaign', 'created_by_id')

        # Deleting field 'Campaign.updated'
        db.delete_column(u'referral_campaign', 'updated')

        # Deleting field 'Campaign.updated_by'
        db.delete_column(u'referral_campaign', 'updated_by_id')

        # Adding field 'Referrer.sender'
        db.add_column(u'referral_referrer', 'sender',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['auth.User']),
                      keep_default=False)

        # Deleting field 'Referrer.state'
        db.delete_column(u'referral_referrer', 'state')

        # Deleting field 'Referrer.created'
        db.delete_column(u'referral_referrer', 'created')

        # Deleting field 'Referrer.created_by'
        db.delete_column(u'referral_referrer', 'created_by_id')

        # Deleting field 'Referrer.updated'
        db.delete_column(u'referral_referrer', 'updated')

        # Deleting field 'Referrer.updated_by'
        db.delete_column(u'referral_referrer', 'updated_by_id')


    models = {
        u'actstream.action': {
            'Meta': {'ordering': "('-timestamp',)", 'object_name': 'Action'},
            'action_object_content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'action_object'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'action_object_object_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'actor_content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'actor'", 'to': u"orm['contenttypes.ContentType']"}),
            'actor_object_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'batch_time_minutes': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_batchable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'state': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'}),
            'target_content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'target'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'target_object_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'timestamp_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'verb': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'relationships': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'related_to'", 'symmetrical': 'False', 'through': u"orm['relationships.Relationship']", 'to': u"orm['auth.User']"}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'referral.campaign': {
            'Meta': {'ordering': "['name']", 'object_name': 'Campaign'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'campaign_created_by'", 'to': u"orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pattern': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'state': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'campaign_updated_by'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'referral.referrer': {
            'Meta': {'ordering': "['name']", 'object_name': 'Referrer'},
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'referrers'", 'null': 'True', 'to': u"orm['referral.Campaign']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'referrer_created_by'", 'to': u"orm['auth.User']"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'state': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'referrer_updated_by'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'referral.userreferrer': {
            'Meta': {'ordering': "['referrer__name']", 'object_name': 'UserReferrer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'referrer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'users'", 'to': u"orm['referral.Referrer']"}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'user_referrer'", 'unique': 'True', 'to': u"orm['auth.User']"})
        },
        u'relationships.relationship': {
            'Meta': {'ordering': "('created',)", 'unique_together': "(('from_user', 'to_user', 'status', 'site'),)", 'object_name': 'Relationship'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'from_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'from_users'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'related_name': "'relationships'", 'to': u"orm['sites.Site']"}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['relationships.RelationshipStatus']"}),
            'to_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'to_users'", 'to': u"orm['auth.User']"}),
            'weight': ('django.db.models.fields.FloatField', [], {'default': '1.0', 'null': 'True', 'blank': 'True'})
        },
        u'relationships.relationshipstatus': {
            'Meta': {'ordering': "('name',)", 'object_name': 'RelationshipStatus'},
            'from_slug': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'symmetrical_slug': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'to_slug': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'verb': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['referral']