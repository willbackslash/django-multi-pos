from django.core.management.sql import emit_post_migrate_signal
from django.db import migrations


def up(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    emit_post_migrate_signal(2, False, db_alias)
    Group = apps.get_model("auth", "Group")
    Group.objects.using(db_alias).bulk_create(
        [Group(name="company_master_user"), Group(name="branch_master_user")]
    )

    Permission = apps.get_model("auth", "Permission")
    can_create_users_for_his_branch = Permission.objects.get(
        codename__exact="can_create_users_for_his_branch"
    )
    can_create_users_for_his_company = Permission.objects.get(
        codename__exact="can_create_users_for_his_company"
    )

    company_master_user_group = Group.objects.using(db_alias).get(
        name__exact="company_master_user"
    )
    company_master_user_group.permissions.add(
        can_create_users_for_his_branch, can_create_users_for_his_company
    )

    branch_master_user_group = Group.objects.using(db_alias).get(
        name__exact="branch_master_user"
    )
    branch_master_user_group.permissions.add(can_create_users_for_his_branch)


def down(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Group.objects.filter(
        name__in=["company_master_user", "branch_master_user"]
    ).delete()


class Migration(migrations.Migration):
    dependencies = [("users", "0002_auto_20200830_0016")]
    operations = [migrations.RunPython(up, down)]
