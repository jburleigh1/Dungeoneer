from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.db.models import Q
from django.db.models import Sum

from charactermanager.models import Ability, AbilityKeyword, Character, Campaign, MonsterCategory, Monster, Weapon, Item, FeatBonus, ClassBonus
from charactermanager.forms import CharacterModelForm

from itertools import chain


class Counter:
    count = 0
    
    def __unicode__(self):
        return count

    def increment(self):
        self.count += 1
        return self.count

    def decrement(self):
        self.count -= 1
        return self.count

def campaign(request, campaign_name):
    context = RequestContext(request)
    context['campaign'] = get_object_or_404(Campaign,slug=campaign_name)
    return render_to_response('dungeoneer/campaignTemplate.html', context)

def campaigns(request):
    context = RequestContext(request)
    context['campaigns'] = Campaign.objects.all().order_by('name')
    return render_to_response('dungeoneer/campaignListTemplate.html', context)

def abilities(request, campaign_name, player_name):
    get_object_or_404(Character,~Q(enabled=False),slug=player_name)
    context = RequestContext(request)
    context['counter'] = Counter()
    context['name'] = player_name
    context['level'] = Character.objects.filter(slug=player_name).values_list('level',flat=True).get()
    context['strength'] = Character.objects.filter(slug=player_name).values_list('strength',flat=True).get()
    context['constitution'] = Character.objects.filter(slug=player_name).values_list('constitution',flat=True).get()
    context['dexterity'] = Character.objects.filter(slug=player_name).values_list('dexterity',flat=True).get()
    context['intelligence'] = Character.objects.filter(slug=player_name).values_list('intelligence',flat=True).get()
    context['wisdom'] = Character.objects.filter(slug=player_name).values_list('wisdom',flat=True).get()
    context['charisma'] = Character.objects.filter(slug=player_name).values_list('charisma',flat=True).get()
    # Primary Weapon
    context['primaryProf'] = Character.objects.filter(slug=player_name).values_list('primaryProf',flat=True).get()
    primaryFeatBonusIds = Character.objects.filter(slug=player_name).values_list('primaryFeatBonus',flat=True)
    primaryFeatBonus = FeatBonus.objects.filter(pk__in=primaryFeatBonusIds) 
    context['primaryFeatBonus'] = FeatBonus.objects.filter(pk__in=primaryFeatBonusIds) 
    context['primaryFeatBonusTotal'] = primaryFeatBonus.aggregate(Sum('bonus'))
    primaryClassBonusIds = Character.objects.filter(slug=player_name).values_list('primaryClassBonus',flat=True)
    primaryClassBonus = ClassBonus.objects.filter(pk__in=primaryClassBonusIds) 
    context['primaryClassBonus'] = ClassBonus.objects.filter(pk__in=primaryClassBonusIds) 
    context['primaryClassBonusTotal'] = primaryClassBonus.aggregate(Sum('bonus'))
    primaryWeaponId = Character.objects.filter(slug=player_name).values_list('primaryWeapon',flat=True)
    try:
        context['primaryWeapon'] = Weapon.objects.get(pk__in=primaryWeaponId)
    except Weapon.DoesNotExist: 
        context['primaryWeapon'] = None
    primaryItemBonusIds = Character.objects.filter(slug=player_name).values_list('primaryItems',flat=True)
    primaryItemBonus = Item.objects.filter(pk__in=primaryItemBonusIds)
    context['primaryItemBonus'] = Item.objects.filter(pk__in=primaryItemBonusIds)
    context['primaryItemBonusTotal'] = primaryItemBonus.aggregate(Sum('bonus'))
    # Secondry Weapon
    context['secondaryProf'] = Character.objects.values_list('secondaryProf',flat=True).get(pk=1)
    secondaryFeatBonusIds = Character.objects.filter(slug=player_name).values_list('secondaryFeatBonus',flat=True)
    secondaryFeatBonus = FeatBonus.objects.filter(pk__in=secondaryFeatBonusIds) 
    context['secondaryFeatBonus'] = FeatBonus.objects.filter(pk__in=secondaryFeatBonusIds) 
    context['secondaryFeatBonusTotal'] = secondaryFeatBonus.aggregate(Sum('bonus'))
    secondaryClassBonusIds = Character.objects.filter(slug=player_name).values_list('secondaryClassBonus',flat=True)
    secondaryClassBonus = ClassBonus.objects.filter(pk__in=secondaryClassBonusIds) 
    context['secondaryClassBonus'] = ClassBonus.objects.filter(pk__in=secondaryClassBonusIds) 
    context['secondaryClassBonusTotal'] = secondaryClassBonus.aggregate(Sum('bonus'))
    secondaryWeaponId = Character.objects.filter(slug=player_name).values_list('secondaryWeapon',flat=True)
    try:
        context['secondaryWeapon'] = Weapon.objects.get(pk__in=secondaryWeaponId)
    except Weapon.DoesNotExist: 
        context['secondaryWeapon'] = None
    secondaryItemBonusIds = Character.objects.filter(slug=player_name).values_list('secondaryItems',flat=True)
    secondaryItemBonus = Item.objects.filter(pk__in=secondaryItemBonusIds)
    context['secondaryItemBonus'] = Item.objects.filter(pk__in=secondaryItemBonusIds)
    context['secondaryItemBonusTotal'] = secondaryItemBonus.aggregate(Sum('bonus'))
    # Extra Weapon
    context['extraProf'] = Character.objects.values_list('extraProf',flat=True).get(pk=1)
    extraFeatBonusIds = Character.objects.filter(slug=player_name).values_list('extraFeatBonus',flat=True)
    extraFeatBonus = FeatBonus.objects.filter(pk__in=extraFeatBonusIds) 
    context['extraFeatBonus'] = FeatBonus.objects.filter(pk__in=extraFeatBonusIds) 
    context['extraFeatBonusTotal'] = extraFeatBonus.aggregate(Sum('bonus'))
    extraClassBonusIds = Character.objects.filter(slug=player_name).values_list('extraClassBonus',flat=True)
    extraClassBonus = ClassBonus.objects.filter(pk__in=extraClassBonusIds) 
    context['extraClassBonus'] = ClassBonus.objects.filter(pk__in=extraClassBonusIds) 
    context['extraClassBonusTotal'] = extraClassBonus.aggregate(Sum('bonus'))
    extraWeaponId = Character.objects.filter(slug=player_name).values_list('extraWeapon',flat=True)
    try:
        context['extraWeapon'] = Weapon.objects.get(pk__in=extraWeaponId)
    except Weapon.DoesNotExist: 
        context['extraWeapon'] = None
    extraItemBonusIds = Character.objects.filter(slug=player_name).values_list('extraItems',flat=True)
    extraItemBonus = Item.objects.filter(pk__in=extraItemBonusIds)
    context['extraItemBonus'] = Item.objects.filter(pk__in=extraItemBonusIds)
    context['extraItemBonusTotal'] = extraItemBonus.aggregate(Sum('bonus'))
    # Abilities
    atwills = Ability.objects.filter(character__slug=player_name, recharge="ATWILL").order_by('name')
    encounters = Ability.objects.filter(character__slug=player_name, recharge="ENCOUNTER").order_by('name')
    dailies = Ability.objects.filter(character__slug=player_name, recharge="DAILY").order_by('name')
    context['abilities'] = list( chain(atwills, encounters, dailies) )
    context['recharges'] = Ability.objects.filter(character__slug=player_name).values_list('recharge', flat=True).distinct()
    context['actionTypes'] = Ability.objects.filter(character__slug=player_name).values_list('actionType', flat=True).distinct()   
    keywordIds = Ability.objects.filter(character__slug=player_name).values_list('keywords', flat=True).distinct()
    context['keywords'] = AbilityKeyword.objects.filter(pk__in=keywordIds)
    return render_to_response('dungeoneer/abilitiesTemplate.html', context)

def edit_user(request, player_name=None):
    context = RequestContext(request)
    if(player_name != None):
        player = Character.objects.filter(slug=player_name)
    else:
        player = None

    if request.method == 'GET':
        form = CharacterModelForm()
    else:
        form = CharacterModelForm(player)

    context['player'] = player
    context['form'] = form
    return render_to_response('dungeoneer/characterFormTemplate.html', context)



def monsters(request):
    context = RequestContext(request)
    context['categories'] = MonsterCategory.objects.all().order_by('name')
#     = {}
#    for category in categories:
#        context['categories'][category.name] = {}
#        for subCategory in category.subCategories.all():
#            context['categories'][category.name][subCategory.name] = {}
#            context['categories'][category.name][subCategory.name]['monsters'] = Monster.objects.filter(category=category.id,subCategory=subCategory.id)
#        context['categories'][category.name]['monsters'] = Monster.objects.filter(category=category.id,subCategory__isnull=True)
    return render_to_response('dungeoneer/monsterListTemplate.html', context)



def handler404(request):
    response = render_to_response('dungeoneer/404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response

def handler500(request):
    response = render_to_response('dungeoneer/500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
