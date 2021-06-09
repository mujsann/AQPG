storyname = 'doometernal'

Story = """
eight months after the events of 2016's doom, earth has been overrun by demonic forces, wiping out 60% of the planet's population, under the now-corrupted union aerospace corporation. what remains of humanity has either fled earth or have banded together as part of Arc, a resistance movement formed to stop the invasion but have gone into hiding after suffering heavy losses.
the doom slayer, having previously been betrayed and teleported away by dr samuel hayden, returns with a satellite fortress controlled by the ai vega to quell the demonic invasion by killing the hell priests; deags nilox, ranak, and grav. the priests serve an angelic being known as the khan maykr who seeks to sacrifice mankind the slayer teleports to a destroyed los angeles and kills deag nilox, but the khan maykr teleports the two remaining priests to unknown locations, forcing the slayer to continue searching. 

after retrieving a celestial locator from the sentinel world of exultia, the slayer travels to hell to retrieve a power source from a fallen sentinel known as the betrayer. he warns the slayer that humanity's time has come before giving him the power source and a special dagger. vega directs the slayer to a citadel in the arctic where deag ranak has taken refuge, and the slayer kills him after defeating his guardian doom hunters. in response, the khan maykr moves deag grav to a hidden location and accelerates the invasion of earth 

forced to change tactics, the slayer destroys the super gore nest in central europe, where the invasion began. with no leads on finding the last hell priest, vega suggests finding hayden, who knows the location of deag grav. the slayer makes his way to an arc compound where he retrieves hayden's robotic shell, as well as the crucible before facing a marauder, a demonic sentinel sent to stop the slayer.

upon uploading hayden's mind into the fortress, he reveals deag grav is hiding on sentinel prime with the only portal to sentinel prime located in the ancient city of hebeth in mars' core, to which there is no immediate access. the slayer then travels to a facility on phobos where he uses the bfg 10000 to shoot a hole in mars, which he uses to reach hebeth. after reaching sentinel prime, flashbacks reveal the slayer to be doomguy. found badly wounded by sentinels, doomguy was brought before the deags and was forced to fight in a gladiatorial arena. impressed by doomguy’s ruthlessness in battle, the deags inducted him into the sentinels, while the khan maykr inquires into doomguy's knowledge of the demons. in the present, the slayer finds deag grav in the arena and defeats a massive demon known as the gladiator. despite knowing that it is against sentinel law to murder deag grav on sacred ground, the slayer kills him anyways and returns to the fortress.upon his return, the slayer's fortress is shut down remotely by the khan maykr to prevent any further interference in her plans 

she reveals her intentions to resurrect the demon world-eating super-predator, the icon of sin, to consume mankind before having the slayer attacked by demons. surviving the ambush, the slayer uses the demonic crucible's latent argent energy to reactivate the fortress and travels to argent d'nur to retrieve his own crucible from his time in the sentinels.furher flashbacks reveal that during the ill-fated battle of argent d'nur, a rogue maykr known as the ' 'seraphim had imbued doomguy with superhuman abilities, transforming him into the doom slayer. after retrieving the hilt of the crucible, it is revealed that the khan maykr formed an alliance with hell to produce argent energy, which is created through the mass sacrifice of human souls 

in return for providing worlds for hell to invade, the maykrs receive a share of the argent energy produced by hell which allows their own dimension, urdak, to survive. 

hayden directs the slayer through hell's massive citadel, nekravol, until he finds a portal leading to the urdak. he then finds the khan maykr and halts the awakening ceremony by using the betrayer's dagger to destroy the icon's heart. free from maykr control, the icon of sin awakens from its dormant state and teleports to earth. with the dimensional barrier destroyed, the demons break their pact with the maykrs and proceed to invade urdak. the khan maykr confronts the slayer, saying that urdak must destroy earth to survive. they battle and the slayer kills the khan maykr before taking a portal back to earth to confront the icon of sin, although vega is left behind to ensure the portal stays open. after an intense battle across the cityscape, the slayer kills the icon of sin by stabbing it in the head with the crucible, putting an end to hell's invasion of earth. as the slayer walks away, king novik, leader of the night sentinels, states how the slayer's fight is eternal
"""

Entities = {'Slayer': 'Player',
             'ballista': 'weapon',
             'bfg': 'weapon',
             'chaingun': 'weapon',
             'chainsaw': 'weapon',
             'canon': 'weapon',
             'hook': 'weapon',
             'rifle': 'weapon',
             'shotgun': 'weapon',
             'super gore nest': 'location',
             'nest':'location',
             'ARC compound': 'location',
            'rocket launcher': 'weapon',
             'crucible': 'weapon',
             'unmaykr': 'weapon',
             'pistol': 'weapon',
             'hell': 'location',
             'Exultia': 'location' ,
            'Base': 'location',
             'Doom Hunter Base': 'location',
             'Arc': 'location',
             'Mars': 'location',
             'Sentinel Prime':'location',
             'Taras Nabad': 'location',
             'phobos':'facility',
             'Nekravol': 'location',
             'Urdak': 'location',
             'Sin': 'location',
             'los angeles': 'location',
             'angeles':'location',
             'Totem': 'monster',
             'Cueball':'monster',
             'tentacle': 'monster',
             'garygoyle': 'enemy',
             'imp':'enemy',
             'lost soul': 'enemy' ,
             'soldier': 'enemy',
             'zombies': 'enemy',
            'Arachnotron':'enemy',
             'Cacodemon Carcass': 'enemy',
             'Cyber Mancubus': 'enemy',
             'Knight': 'enemy',
             'Maykr' : 'enemy',
            'Mancubus': 'enemy',
             'Pain Elemental': 'enemy',
             'Pinky': 'enemy',
             'Prowler': 'enemy',
             'Revenant': 'enemy',
             'Spectre': 'enemy',
             'Whiplash': 'enemy',
            'Archvile': 'enemy',
             'Baron of Hell': 'enemy',
             'Doom Hunter': 'enemy',
             'Marauder': 'enemy',
             'Tyrant': 'enemy',
             'gladiator': 'enemy',
            'khan maykr': 'enemy',
             'icon of sin': 'enemy',
             'satellite fortress': 'item',
             'facility':'facility',
             'present': 'item',
             'battle':'battle',
             'him': 'enemy',
             'deag': 'enemy',
            'demonic': 'weapon',
             'energy':'weapon',
             'icon':'priest' }





player_name = ''
for entity in Entities:
    if Entities[entity].lower() == 'player':
        player_name = entity.lower()
