from django.contrib import admin
from charactermanager.models import Campaign, Item, Character, Weapon, Ability, AbilityKeyword, Monster, MonsterPower, MonsterCategory, MonsterSubCategory, MonsterKeyword, FeatBonus, ClassBonus

class CampaignAdmin(admin.ModelAdmin):
    filter_horizontal = ('characters', )

class CharacterAdmin(admin.ModelAdmin):
    filter_horizontal = ('abilities','primaryItems','secondaryItems','extraItems','primaryFeatBonus','extraFeatBonus','primaryClassBonus','secondaryFeatBonus','secondaryClassBonus','extraClassBonus')
    suit_form_tabs = (('general', 'General'), ('stats', 'Stats'), ('primary-weapon', 'Primary Weapon'), ('secondary-weapon', 'Secondary Weapon'), ('extra-weapon', 'Extra Weapon'))
    fieldsets = [
    ('General', {
        'classes': ('suit-tab', 'suit-tab-general',),
        'fields': ['name', 'slug', 'enabled', 'image', 'abilities', 'summary', 'background']
    }),('Stats',{
        'classes': ('suit-tab', 'suit-tab-stats',),
        'fields': ['level', 'strength', 'constitution', 'dexterity', 'intelligence', 'wisdom', 'charisma']
    }),('Primary Weapon',{
        'classes': ('suit-tab', 'suit-tab-primary-weapon',),
        'fields': ['primaryWeaponName', 'primaryWeapon', 'primaryProf', 'primaryItems', 'primaryFeatBonus','primaryClassBonus']
    }),('Secondary Weapon',{
        'classes': ('suit-tab', 'suit-tab-secondary-weapon',),
        'fields': ['secondaryWeaponName', 'secondaryWeapon', 'secondaryProf', 'secondaryItems', 'secondaryFeatBonus','secondaryClassBonus']
    }),('Extra Weapon',{
        'classes': ('suit-tab', 'suit-tab-extra-weapon',),
        'fields': ['extraWeaponName', 'extraWeapon', 'extraProf', 'extraItems', 'extraFeatBonus','extraClassBonus']
    }
    )]
    
class AbilityAdmin(admin.ModelAdmin):
    save_as = True
    filter_horizontal = ('keywords', )
    
class WeaponAdmin(admin.ModelAdmin):
    save_as = True
    
class ItemAdmin(admin.ModelAdmin):
    save_as = True
    
class FeatAdmin(admin.ModelAdmin):
    save_as = True
    
class ClassAdmin(admin.ModelAdmin):
    save_as = True

class MonsterAdmin(admin.ModelAdmin):
    save_as = True
    filter_horizontal = ('keywords','auraKeywords')
    
class MonsterPowerAdmin(admin.ModelAdmin):
    save_as = True
    filter_horizontal = ('keywords',)

admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Character, CharacterAdmin)
admin.site.register(Ability, AbilityAdmin)
admin.site.register(AbilityKeyword)
admin.site.register(Weapon, WeaponAdmin)
admin.site.register(Item)
admin.site.register(FeatBonus)
admin.site.register(ClassBonus)

admin.site.register(Monster, MonsterAdmin)
admin.site.register(MonsterPower, MonsterPowerAdmin)
admin.site.register(MonsterKeyword)
admin.site.register(MonsterCategory)
admin.site.register(MonsterSubCategory)