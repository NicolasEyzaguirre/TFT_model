import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os 

def ubicacion():
    current_directory = os.getcwd()
    parent_directory = os.path.dirname(current_directory)
    os.chdir(parent_directory)


def limpieza (show=False,plot=0):

    Data=pd.read_csv('Data/Train.csv')

    items_=Data.columns[Data.columns.str.contains(r'(_item\d$)')]

    for column in items_:
        Data[column].replace(regex=r'^\w+\w$', value='1',inplace=True)

    Data[items_] = Data[items_].fillna(0)

    Data[items_]=Data[items_].astype(float)

    for name in Data.select_dtypes("number"):
        Data[name] = Data[name].fillna(0)

    for name in Data.select_dtypes("object"):
        Data[name] = Data[name].fillna("None")

    Data['augment0']=Data['augment0'].str.split('_').str.get(-1)
    Data['augment1']=Data['augment1'].str.split('_').str.get(-1)
    Data['augment2']=Data['augment2'].str.split('_').str.get(-1)



    names=['Aatrox_item', 'Anivia_item','AoShin_item','Ashe_item','AurelionSol_item','Bard_item','Braum_item','Corki_item','Diana_item',
       'DragonBlue_item','DragonGold_item','DragonGreen_item','DragonPurple_item','Elise_item','Ezreal_item','Gnar_item','Hecarim_item',
       'Heimerdinger_item','Illaoi_item','Jinx_item','Karma_item','Kayn_item','LeeSin_item','Leona_item','Lillia_item','Lulu_item','Nami_item',
       'Neeko_item','Nidalee_item','Nunu_item','Nunu_item','Ornn_item','Pyke_item','Qiyana_item','Ryze_item','Sejuani_item','Senna_item',
       'Sett_item','Shen_item','Shyvana_item','Skarner_item','Sona_item','Soraka_item','Swain_item','Sylas_item','TahmKench_item','Talon_item',
       'Taric_item','Thresh_item','TrainerDragon_item','Tristana_item','Twitch_item','Varus_item','Vladimir_item','Volibear_item','Xayah_item',
       'Yasuo_item','Yone_item','Zoe_item']
    for a in names:
        Data[a]=Data.loc[:,'TFT7_'+a+'0':'TFT7_'+a+'2'].sum(axis=1)

    Data.drop(items_,axis=1,inplace=True)

    a=Data.columns[Data.columns.str.startswith('TFT7_')]
    b=a.str.split('TFT7_').str.get(-1)
    name=0
    for i in a:
        Data.rename(columns = {i:b[name]},inplace=True)
        name=name+1
    Aumentos_tipos= { 
    'Ascension':1,
    'AxiomArc1': 1,'AxiomArc2': 1,
    'BestFriends1':1,'BestFriends2':1, 'BestFriends3': 1,
    'BetterTogether': 1,
    'BigFriend': 1,'BigFriend2':1,
    'BinaryAirdrop':1,
    'Bloodlust1':1,'Bloodlust2':1,'Bloodlust3':1,
    'BlueBattery2': 1,
    'CelestialBlessing1': 1,'CelestialBlessing2': 1, 'CelestialBlessing3':1,
    'CombatTraining1': 1, 'CombatTraining2': 1,'CombatTraining3': 1,
    'CyberneticImplants1': 1,'CyberneticImplants2':1, 'CyberneticImplants3':1,
    'CyberneticShell1':1,'CyberneticShell2':1,'CyberneticShell3':1,
    'CyberneticUplink1':1,'CyberneticUplink2':1,'CyberneticUplink3':1,
    'Diversify1': 1,'Diversify2': 1, 'Diversify3': 1,
    'Distancing':1,'Distancing2':1, 'Distancing3':1,
    'Electrocharge1':1,'Electrocharge2':1,'Electrocharge3':1,
    'Featherweights1':1,'Featherweights2':1,'Featherweights3':1,
    'FirstAidKit': 1, 'FirstAidKit2': 1,
    'ForceOfNature':1,
    'FuturePeepers':1,'FuturePeepers2':1,
    'GadgetExpert': 1,
    'JeweledLotus':1,
    'LudensEcho1': 1, 'LudensEcho2':1,'LudensEcho3': 1,
    'MakeshiftArmor1':1,'MakeshiftArmor2':1,'MakeshiftArmor3':1,
    'Meditation1':1,'Meditation2':1,'Meditation3':1,
    'MetabolicAccelerator':1,
    'Preparation': 1, 'Preparation2':1,'Preparation3':1, 'Preparation1HR':1,'Preparation2HR':1,'Preparation3HR':1,
    'PortableForge':1,
    'PandorasItems':1,
    'SalvageBin':1,
    'SecondWind1':1,'SecondWind2':1,
    'SunfireBoard':1,
    'ThreesCompany':1,
    'TargetDummies': 1,
    'ThrillOfTheHunt1': 1, 'ThrillOfTheHunt2': 1,
    'TinyTitans':1,
    'TriForce1':1,'TriForce2':1,'TriForce3':1,
    'TrueTwos':1,
    'Twins1':1,'Twins2':1,'Twins3':1,
    'VerdantVeil':1,
    'Weakspot':1,

    'AstralIntercosmicGifts': 1,
    'AssassinCutthroat': 1,
    'BruiserTitanicStrength': 1, 'BruiserPersonalTraining':1,'BruiserPersonalTrainerHR':1,
    'CannoneerHotShot': 1, 'CannoneerRicochet': 1,
    'CavalierForAllUnits':1,
    'CavalierDevastatingCharge': 1,
    'DragonAlliance': 1, 'DragonHorde': 1,'DragonmancerInspire': 1,'EvokerEssenceTheft': 1,
    'GuardianHeroicPresence':1,
    'GuildLoot':1,'GuildLootHR':1, 'GuildGearUpgrades':1, 
    'JadePenitence': 1,'JadeEternalProtection': 1,
    'MirageHallucinate': 1,
    'ShapeshifterBeastsDen': 1,
    'TrainerSecretSnax': 1, 
    'TempestEyeOfTheStorm': 1,
    'RevelPartyFavors':1, 'RevelPartyFavorsHR':1,'RevelPartyTime': 1,
    'RagewingScorch': 1,'RagewingTantrum':1,
    'ScalescornNomads': 1,
    'SwiftshotPressTheAttack': 1,    
    'ShimmerscaleRecklessSpending': 102,'ShimmerscaleSpending':1, 
    'WarriorTiamat': 1,
    'WhisperTwilightUmbrage': 1,
    
    


   
    'AFK': 2,'AFKHR':2,
    'AncientArchives':2,'AncientArchives2':2,
    'BandOfThieves1': 2,'BandOfThieves2':2,'BandOfThieves':2,
    'CalculatedLoss':2,
    'ClearMind':2,
    'CursedCrown':2,
    'ClutteredMind': 2,
    'ComponentGrabBag':2, 'GrandGambler': 2,
    'HighEndShopping':2,
    'HyperRoll':2,
    'ItemGrabBag1': 2,'ItemGrabBag2': 2,
    'LategameSpecialist': 2,
    'LastStand': 2,
    'LivingForge': 2,'LivingForgeHR':2,
    'LootMaster': 2,
    'MageConference':2, 'MageConferenceHR':2,
    'MaxLevel10':2,
    'MikaelsGift':2,
    'PandorasBench': 2,
    'RichGetRicher':2,'RichGetRicherPlus': 2,
    'Recombobulator':2,
    'RadiantRelics':2,
    'SacrificialPact':2,  #CruelPact
    'SlowAndSteady':2,
    'ThinkFast':2,
    'TheGoldenEgg':2,'TheGoldenEggHR':2,
    'ThriftShop':2,
    'TradeSectorPlus': 135,'TradeSector':2,
    'UrfsGrabBag1': 2, 'UrfsGrabBag2': 2,
    'Windfall':2,'WindfallPlus':2,'WindfallPlusPlus':2,
    
    

    'AstralTrait':3,
    'AssassinTrait':3,'AssassinTrait2':3,'AssassinEmblem':3,'AssassinEmblem2':3,
    'BruiserTrait':3,'BruiserTrait2':3,'BruiserEmblem':3,'BruiserEmblem2':3,
    'CavalierTrait':3, 'CavalierTrait2':3,'CavalierEmblem':3,'CavalierEmblem2':3,
    'CannoneerTrait':3,'CannoneerTrait2':3,'CannoneerEmblem':3,'CannoneerEmblem2':3,
    'DragonmancerTrait':3,'DragonmancerTrait2':3,'DragonmancerEmblem':3,'DragonmancerEmblem2':3,
    'EvokerTrait':3,'EvokerTrait2':3,'EvokerEmblem':3,'EvokerEmblem2':3,
    'GuardianTrait':3,'GuardianTrait2':3,'GuardianEmblem':3,'GuardianEmblem2':3,
    'GuildTrait':3,'GuildTrait2':3,'GuildEmblem':3,'GuildEmblem2':3,
    'JadeTrait':3,'JadeTrait2':3,'JadeEmblem':3,'JadeEmblem2':3,
    'MysticTrait':3,'MysticTrait2':3,'MysticEmblem':3,'MysticEmblem2':3,
    'MirageTrait':3,'MirageEmblem':3,'MirageEmblem2':3,
    'MageTrait':3,'MageTrait2':3,'MageEmblem':3,'MageEmblem2':3,
    'RevelTrait':3,'RevelTrait2':3,'RevelEmblem':3,'RevelEmblem2':3,
    'RagewingTrait':3,'RagewingTrait2':3,'RagewingEmblem':3,'RagewingEmblem2':3,
    'SwiftshotTrait':3,'SwiftshotTrait2':3,'SwiftshotEmblem':3,'SwiftshotEmblem2':3,
    'ShimmerscaleTrait':3,'ShimmerscaleTrait2':3,'ShimmerscaleEmblem':3,'ShimmerscaleEmblem2':3,
    'ShapeshifterTrait':3,'ShapeshifterTrait2':3,'ShapeshifterEmblem':3,'ShapeshifterEmblem2':3,
    'ScalescornTrait':3,'ScalescornTrait2':3,'ScalescornEmblem':3,'ScalescornEmblem2':3,
    'TempestTrait':3,'TempestTrait2':3,'TempestEmblem':3,'TempestEmblem2':3,
    'Traitless1':3,'Traitless2':3,'Traitless3':3, 
    'TomeOfTraits1':3,'TomeOfTraits2':3,
    'WhispersTrait':3,'WhispersTrait2':3,'WhispersEmblem':3,'WhispersEmblem2':3,
    'WarriorTrait':3,'WarriorTrait2':3,'WarriorEmblem':3,'WarriorEmblem2':3,

    'None':0,  
       
       
    }

    Data['augment0'] = Data['augment0'].replace(Aumentos_tipos)
    Data['augment1'] = Data['augment1'].replace(Aumentos_tipos)
    Data['augment2'] = Data['augment2'].replace(Aumentos_tipos)
    Data[['augment0','augment1','augment2']]=Data[['augment0','augment1','augment2']].astype(int)
    id_keys=list(Data['match_id'].unique())

    test_values = list(np.arange(1, 6144, 1))
    id_dictionary = {}
    for key in id_keys:
        for value in test_values:
            id_dictionary[key] = value
            test_values.remove(value)
            break

    Data['match_id'] = Data['match_id'].replace(id_dictionary)
    if plot==1:

        plt.figure(figsize=(20,5))


        plt.subplot(131)
        sns.set(rc={'figure.figsize':(13,8)})
        sns.countplot(data=Data[Data['Set7_Assassin']>0], x='Set7_Assassin', hue='placement')
        sns.despine()

        plt.subplot(132)
        sns.set(rc={'figure.figsize':(13,8)})
        sns.countplot(data=Data[Data['Set7_Astral']>0], x='Set7_Astral', hue='placement')
        sns.despine()

        plt.subplot(133)
        sns.set(rc={'figure.figsize':(13,8)})
        sns.countplot(data=Data[Data['Set7_Mage']>0], x='Set7_Mage', hue='placement')
        sns.despine()

    if plot==2:
        plt.figure(figsize=(20,5))

        plt.subplot(131)
        sns.set(rc={'figure.figsize':(13,8)})
        sns.countplot(data=Data, x='augment0', hue='placement')
        sns.despine()

        plt.subplot(132)
        sns.set(rc={'figure.figsize':(13,8)})
        sns.countplot(data=Data, x='augment1', hue='placement')
        sns.despine()

        plt.subplot(133)
        sns.set(rc={'figure.figsize':(13,8)})
        sns.countplot(data=Data, x='augment2', hue='placement')
        sns.despine()
    
    if plot==3:
        plt.figure(figsize=(20,5))

        plt.subplot(131)
        sns.set(rc={'figure.figsize':(13,8)})
        sns.countplot(data=Data[Data['Olaf']>0], x='Olaf', hue='placement')
        sns.despine()

        plt.subplot(132)
        sns.set(rc={'figure.figsize':(13,8)})
        sns.countplot(data=Data[Data['Nidalee']>0], x='Nidalee', hue='placement')
        sns.despine()

        plt.subplot(133)
        sns.set(rc={'figure.figsize':(13,8)})
        sns.countplot(data=Data[Data['Bard']>0], x='Bard', hue='placement')
        sns.despine()

    if plot==4:
        match=Data[['match_id','placement','augment0','augment1','augment2','Set7_Assassin','Set7_Astral',
                  'Set7_Bard','Set7_Bruiser','Set7_Cannoneer','Set7_Cavalier','Set7_Dragon','Set7_Dragonmancer','Set7_Evoker',
                  'Set7_Guardian','Set7_Guild','Set7_Jade','Set7_Legend','Set7_Mage','Set7_Mirage','Set7_Mystic','Set7_Ragewing',
                  'Set7_Revel','Set7_Scalescorn','Set7_Shapeshifter','Set7_Shimmerscale','Set7_SpellThief','Set7_Starcaller',
                  'Set7_Swiftshot','Set7_Tempest','Set7_Trainer','Set7_Warrior','Set7_Whispers']]
        plt.figure(figsize=(30,30))
        sns.heatmap(match.corr(), annot=True)

    placement = {
        1: 1,
        2: 1,
        3: 1,
        4: 1,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        }
    Data['placement'] = Data['placement'].replace(placement)
    Data.to_csv('Data/Train_clean.csv') 
    if show == True :
        return Data.head(8)
    

def limpieza_2(show=False):
    Data=pd.read_csv('Data/Test.csv')

    items_=Data.columns[Data.columns.str.contains(r'(_item\d$)')]

    for column in items_:
        Data[column].replace(regex=r'^\w+\w$', value='1',inplace=True)

    Data[items_] = Data[items_].fillna(0)

    Data[items_]=Data[items_].astype(float)

    for name in Data.select_dtypes("number"):
        Data[name] = Data[name].fillna(0)

    for name in Data.select_dtypes("object"):
        Data[name] = Data[name].fillna("None")

    Data['augment0']=Data['augment0'].str.split('_').str.get(-1)
    Data['augment1']=Data['augment1'].str.split('_').str.get(-1)
    Data['augment2']=Data['augment2'].str.split('_').str.get(-1)

    names=['Aatrox_item', 'Anivia_item','AoShin_item','Ashe_item','AurelionSol_item','Bard_item','Braum_item','Corki_item','Diana_item',
       'DragonBlue_item','DragonGold_item','DragonGreen_item','DragonPurple_item','Elise_item','Ezreal_item','Gnar_item','Hecarim_item',
       'Heimerdinger_item','Illaoi_item','Jinx_item','Karma_item','Kayn_item','LeeSin_item','Leona_item','Lillia_item','Lulu_item','Nami_item',
       'Neeko_item','Nidalee_item','Nunu_item','Nunu_item','Ornn_item','Pyke_item','Qiyana_item','Ryze_item','Sejuani_item','Senna_item',
       'Sett_item','Shen_item','Shyvana_item','Skarner_item','Sona_item','Soraka_item','Swain_item','Sylas_item','TahmKench_item','Talon_item',
       'Taric_item','Thresh_item','TrainerDragon_item','Tristana_item','Twitch_item','Varus_item','Vladimir_item','Volibear_item','Xayah_item',
       'Yasuo_item','Yone_item','Zoe_item']
    for a in names:
        Data[a]=Data.loc[:,'TFT7_'+a+'0':'TFT7_'+a+'2'].sum(axis=1)

    Data.drop(items_,axis=1,inplace=True)

    a=Data.columns[Data.columns.str.startswith('TFT7_')]
    b=a.str.split('TFT7_').str.get(-1)
    name=0
    for i in a:
        Data.rename(columns = {i:b[name]},inplace=True)
        name=name+1
    Aumentos_tipos= { 
    'Ascension':1,
    'AxiomArc1': 1,'AxiomArc2': 1,
    'BestFriends1':1,'BestFriends2':1, 'BestFriends3': 1,
    'BetterTogether': 1,
    'BigFriend': 1,'BigFriend2':1,
    'BinaryAirdrop':1,
    'Bloodlust1':1,'Bloodlust2':1,'Bloodlust3':1,
    'BlueBattery2': 1,
    'CelestialBlessing1': 1,'CelestialBlessing2': 1, 'CelestialBlessing3':1,
    'CombatTraining1': 1, 'CombatTraining2': 1,'CombatTraining3': 1,
    'CyberneticImplants1': 1,'CyberneticImplants2':1, 'CyberneticImplants3':1,
    'CyberneticShell1':1,'CyberneticShell2':1,'CyberneticShell3':1,
    'CyberneticUplink1':1,'CyberneticUplink2':1,'CyberneticUplink3':1,
    'Diversify1': 1,'Diversify2': 1, 'Diversify3': 1,
    'Distancing':1,'Distancing2':1, 'Distancing3':1,
    'Electrocharge1':1,'Electrocharge2':1,'Electrocharge3':1,
    'Featherweights1':1,'Featherweights2':1,'Featherweights3':1,
    'FirstAidKit': 1, 'FirstAidKit2': 1,
    'ForceOfNature':1,
    'FuturePeepers':1,'FuturePeepers2':1,
    'GadgetExpert': 1,
    'JeweledLotus':1,
    'LudensEcho1': 1, 'LudensEcho2':1,'LudensEcho3': 1,
    'MakeshiftArmor1':1,'MakeshiftArmor2':1,'MakeshiftArmor3':1,
    'Meditation1':1,'Meditation2':1,'Meditation3':1,
    'MetabolicAccelerator':1,
    'Preparation': 1, 'Preparation2':1,'Preparation3':1, 'Preparation1HR':1,'Preparation2HR':1,'Preparation3HR':1,
    'PortableForge':1,
    'PandorasItems':1,
    'SalvageBin':1,
    'SecondWind1':1,'SecondWind2':1,
    'SunfireBoard':1,
    'ThreesCompany':1,
    'TargetDummies': 1,
    'ThrillOfTheHunt1': 1, 'ThrillOfTheHunt2': 1,
    'TinyTitans':1,
    'TriForce1':1,'TriForce2':1,'TriForce3':1,
    'TrueTwos':1,
    'Twins1':1,'Twins2':1,'Twins3':1,
    'VerdantVeil':1,
    'Weakspot':1,

    'AstralIntercosmicGifts': 1,
    'AssassinCutthroat': 1,
    'BruiserTitanicStrength': 1, 'BruiserPersonalTraining':1,'BruiserPersonalTrainerHR':1,
    'CannoneerHotShot': 1, 'CannoneerRicochet': 1,
    'CavalierForAllUnits':1,
    'CavalierDevastatingCharge': 1,
    'DragonAlliance': 1, 'DragonHorde': 1,'DragonmancerInspire': 1,'EvokerEssenceTheft': 1,
    'GuardianHeroicPresence':1,
    'GuildLoot':1,'GuildLootHR':1, 'GuildGearUpgrades':1, 
    'JadePenitence': 1,'JadeEternalProtection': 1,
    'MirageHallucinate': 1,
    'ShapeshifterBeastsDen': 1,
    'TrainerSecretSnax': 1, 
    'TempestEyeOfTheStorm': 1,
    'RevelPartyFavors':1, 'RevelPartyFavorsHR':1,'RevelPartyTime': 1,
    'RagewingScorch': 1,'RagewingTantrum':1,
    'ScalescornNomads': 1,
    'SwiftshotPressTheAttack': 1,    
    'ShimmerscaleRecklessSpending': 102,'ShimmerscaleSpending':1, 
    'WarriorTiamat': 1,
    'WhisperTwilightUmbrage': 1,
    
    


   
    'AFK': 2,'AFKHR':2,
    'AncientArchives':2,'AncientArchives2':2,
    'BandOfThieves1': 2,'BandOfThieves2':2,'BandOfThieves':2,
    'CalculatedLoss':2,
    'ClearMind':2,
    'CursedCrown':2,
    'ClutteredMind': 2,
    'ComponentGrabBag':2, 'GrandGambler': 2,
    'HighEndShopping':2,
    'HyperRoll':2,
    'ItemGrabBag1': 2,'ItemGrabBag2': 2,
    'LategameSpecialist': 2,
    'LastStand': 2,
    'LivingForge': 2,'LivingForgeHR':2,
    'LootMaster': 2,
    'MageConference':2, 'MageConferenceHR':2,
    'MaxLevel10':2,
    'MikaelsGift':2,
    'PandorasBench': 2,
    'RichGetRicher':2,'RichGetRicherPlus': 2,
    'Recombobulator':2,
    'RadiantRelics':2,
    'SacrificialPact':2,  #CruelPact
    'SlowAndSteady':2,
    'ThinkFast':2,
    'TheGoldenEgg':2,'TheGoldenEggHR':2,
    'ThriftShop':2,
    'TradeSectorPlus': 135,'TradeSector':2,
    'UrfsGrabBag1': 2, 'UrfsGrabBag2': 2,
    'Windfall':2,'WindfallPlus':2,'WindfallPlusPlus':2,
    
    

    'AstralTrait':3,
    'AssassinTrait':3,'AssassinTrait2':3,'AssassinEmblem':3,'AssassinEmblem2':3,
    'BruiserTrait':3,'BruiserTrait2':3,'BruiserEmblem':3,'BruiserEmblem2':3,
    'CavalierTrait':3, 'CavalierTrait2':3,'CavalierEmblem':3,'CavalierEmblem2':3,
    'CannoneerTrait':3,'CannoneerTrait2':3,'CannoneerEmblem':3,'CannoneerEmblem2':3,
    'DragonmancerTrait':3,'DragonmancerTrait2':3,'DragonmancerEmblem':3,'DragonmancerEmblem2':3,
    'EvokerTrait':3,'EvokerTrait2':3,'EvokerEmblem':3,'EvokerEmblem2':3,
    'GuardianTrait':3,'GuardianTrait2':3,'GuardianEmblem':3,'GuardianEmblem2':3,
    'GuildTrait':3,'GuildTrait2':3,'GuildEmblem':3,'GuildEmblem2':3,
    'JadeTrait':3,'JadeTrait2':3,'JadeEmblem':3,'JadeEmblem2':3,
    'MysticTrait':3,'MysticTrait2':3,'MysticEmblem':3,'MysticEmblem2':3,
    'MirageTrait':3,'MirageEmblem':3,'MirageEmblem2':3,
    'MageTrait':3,'MageTrait2':3,'MageEmblem':3,'MageEmblem2':3,
    'RevelTrait':3,'RevelTrait2':3,'RevelEmblem':3,'RevelEmblem2':3,
    'RagewingTrait':3,'RagewingTrait2':3,'RagewingEmblem':3,'RagewingEmblem2':3,
    'SwiftshotTrait':3,'SwiftshotTrait2':3,'SwiftshotEmblem':3,'SwiftshotEmblem2':3,
    'ShimmerscaleTrait':3,'ShimmerscaleTrait2':3,'ShimmerscaleEmblem':3,'ShimmerscaleEmblem2':3,
    'ShapeshifterTrait':3,'ShapeshifterTrait2':3,'ShapeshifterEmblem':3,'ShapeshifterEmblem2':3,
    'ScalescornTrait':3,'ScalescornTrait2':3,'ScalescornEmblem':3,'ScalescornEmblem2':3,
    'TempestTrait':3,'TempestTrait2':3,'TempestEmblem':3,'TempestEmblem2':3,
    'Traitless1':3,'Traitless2':3,'Traitless3':3, 
    'TomeOfTraits1':3,'TomeOfTraits2':3,
    'WhispersTrait':3,'WhispersTrait2':3,'WhispersEmblem':3,'WhispersEmblem2':3,
    'WarriorTrait':3,'WarriorTrait2':3,'WarriorEmblem':3,'WarriorEmblem2':3,

    'None':0,  
       
       
    }

    Data['augment0'] = Data['augment0'].replace(Aumentos_tipos)
    Data['augment1'] = Data['augment1'].replace(Aumentos_tipos)
    Data['augment2'] = Data['augment2'].replace(Aumentos_tipos)
    Data[['augment0','augment1','augment2']]=Data[['augment0','augment1','augment2']].astype(int)
    id_keys=list(Data['match_id'].unique())

    test_values = list(np.arange(1, 6144, 1))
    id_dictionary = {}
    for key in id_keys:
        for value in test_values:
            id_dictionary[key] = value
            test_values.remove(value)
            break

    Data['match_id'] = Data['match_id'].replace(id_dictionary)
    placement = {
        1: 1,
        2: 1,
        3: 1,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        }
    Data['placement'] = Data['placement'].replace(placement)
    Data.to_csv('Data/Test_clean.csv') 
    if show == True :
        return Data.head(8)
    