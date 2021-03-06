#!/usr/bin/python2.7

settlements = [
    "Anor Londo",
    "Arcadia",
    "Beacon",
    "Blackrock",
    "Blackwalk",
    "Blaviken",
    "Bleakstone",
    "Bloodreach",
    "Bloodstone",
    "Bloodwalk",
    "Caprica",
    "Carthus",
    "Crydee",
    "Daggerfall",
    "Darkover",
    "Darkreach",
    "Darill's Tomb",
    "Darunia",
    "Dawn",
    "Dawnstar",
    "Deadrock",
    "Death Heim",
    "Death Mountain",
    "Doomrock",
    "Dread",
    "Dreadrock",
    "Eastmarch",
    "Eastmost Penninsula",
    "Ember",
    "Emberhold",
    "Emberwatch",
    "Fabul",
    "Fireshrine",
    "First Light",
    "Founder's Rest",
    "Fourhorn",
    "Gloom",
    "Gormrange",
    "Graverock",
    "Gravestone",
    "Haven",
    "Heorot",
    "Home",
    "Hope",
    "Hyrule",
    "Izalith",
    "Kaer Morhen",
    "Kasuto",
    "Kattegat",
    "Keizaal",
    "Lantern's Reach",
    "Last Light",
    "Lightfall",
    "Lufenia",
    "Lux",
    "Melmond",
    "Mido",
    "Mist",
    "Mysidia",
    "Narshe",
    "New Londo",
    "Nilfgaard",
    "Nox",
    "Old Kasuto",
    "Onrac",
    "Proudrock",
    "Pthumeria",
    "Rivia",
    "Rockall",
    "Ruto",
    "Sanctuary",
    "San Junipero",
    "Satan's Lantern",
    "Serenity Valley",
    "Shadow's End",
    "Silent Hill",
    "Solitude",
    "Spectacle Rock",
    "Stonemarch",
    "Stonevale",
    "The Ancient Lantern",
    "The Black Lantern",
    "The Gambler's Lantern",
    "The Gold Lantern",
    "The Silver Lantern",
    "The White Lantern",
    "Three Eye Rock",
    "Tiburn",
    "Vizima",
    "Westmarch",
    "White Rock",
    "Whiterun",
    "Witchweed",
]

male = [
    "Aaron",
    "Achilles",
    "Adam",
    "Aeneas",
    "Aias",
    "Ajax",
    "Akira",
    "Aldrich",
    "Alduin",
    "Alexander",
    "Alucard",
    "Allister",
    "Alva",
    "Anchises",
    "Andrzej",
    "Anton",
    "Armitage",
    "Artorias",
    "Arthur",
    "Asher",
    "Astyanax",
    "Atreyu",
    "Atticus",
    "Augustus",
    "Amos",
    "Batou",
    "Benedict",
    "Borris",
    "Brian",
    "Brooks",
    "Caleb",
    "Caliban",
    "Calvin",
    "Case",
    "Cathbad",
    "Cecil",
    "Clint",
    "Cole",
    "Conan",
    "Croesus",
    "Cuchulain",
    "Cyril",
    "Cyrus",
    "Damon",
    "Dante",
    "Dashiell",
    "Declan",
    "Demetrius",
    "Demarcus",
    "Del",
    "Delita",
    "Deltron",
    "Derek",
    "Diego",
    "Donovan",
    "Draco",
    "Drizzt",
    "Duncan",
    "Edward",
    "Eirik",
    "Eli",
    "Elvis",
    "Errol",
    "Esteban",
    "Ezekiel",
    "Ezra",
    "Felix",
    "Fester",
    "Fidel",
    "Fingal",
    "Finn",
    "Foster",
    "Francis",
    "Gabriel",
    "Gaunther",
    "Gerald",
    "Geralt",
    "Gerard",
    "Giovanni",
    "Gomez",
    "Griffith",
    "Gustavo",
    "Guy",
    "Gwyn",
    "Gyuri",
    "Haakon",
    "Hadrian",
    "Hawkeye",
    "Hector",
    "Hideo",
    "Hipolito",
    "Hiram",
    "Hobbes",
    "Hugh",
    "Humbert",
    "Humberto",
    "Ian",
    "Icarus",
    "Idris",
    "Ignacio",
    "Ike",
    "Irving",
    "Israel",
    "Isaac",
    "Jacob",
    "Jacinto",
    "Jeremy",
    "Jesse",
    "Jaoquin",
    "Jon",
    "Jonah",
    "Jorge",
    "Jude",
    "Julius",
    "Kalameet",
    "Kane",
    "Karl",
    "Khalil",
    "Khoa",
    "Khorvash",
    "Killian",
    "Kieran",
    "Kirk",
    "Klaus",
    "Kris",
    "Kyle",
    "Lambert",
    "Lance",
    "Lazaro",
    "Leif",
    "Leonard",
    "Logan",
    "Liam",
    "Lincoln",
    "Link",
    "Locke",
    "Lucas",
    "Lucien",
    "Lucius",
    "Luther",
    "Lyman",
    "Lysandus",
    "Magnus",
    "Malcolm",
    "Malik",
    "Malvolio",
    "Manannan",
    "Marcus",
    "Mason",
    "Maelcum",
    "Maximo",
    "Maxwell",
    "Maynard",
    "Merlin",
    "Modesto",
    "Mohammed",
    "Morne",
    "Mordack",
    "Moshe",
    "Micah",
    "Mulder",
    "Nathan",
    "Nestor",
    "Nils",
    "Norman",
    "Noah",
    "Oberon",
    "Olaf",
    "Oliver",
    "Orlando",
    "Ozelianho",
    "Owen",
    "Paul",
    "Pawel",
    "Pelagius",
    "Peter",
    "Petrus",
    "Piotr",
    "Preston",
    "Puck",
    "Pug",
    "Quentin",
    "Ramza",
    "Rashad",
    "Ravix",
    "Reuben",
    "Reed",
    "Robb",
    "Robert",
    "Rodin",
    "Reinhardt",
    "Reinaldo",
    "Rico",
    "Rickert",
    "Royal",
    "Raynaldo",
    "Roland",
    "Rolondo",
    "Rolo",
    "Royce",
    "Rubicante",
    "Ryu",
    "Sean",
    "Sergei",
    "Setzer",
    "Sigi",
    "Sigmund",
    "Silas",
    "Shane",
    "Simon",
    "Santiago",
    "Solomon",
    "Sylvester",
    "Sang",
    "Seth",
    "Stark",
    "Talos",
    "Telamon",
    "Tetsuo",
    "Teucer",
    "Thanh",
    "Theron",
    "Theseus",
    "Thor",
    "Timon",
    "Timothy",
    "Titus",
    "Tobias",
    "Trey",
    "Trent",
    "Trevor",
    "Ulf",
    "Ulysses",
    "Umberto",
    "Unferth",
    "Uriel",
    "Valentine",
    "Vaughn",
    "Vesemir",
    "Victor",
    "Vincenzo",
    "Virgil",
    "Vimme",
    "Vivec",
    "Vlad",
    "Voltaire",
    "Ward",
    "Wallace",
    "Wiglaf",
    "William",
    "Wilfred",
    "Xavier",
    "Xerxes",
    "Yang",
    "Zachary",
    "Zane",
    "Zeke",
    "Zhu Di",
    "Zophar",
    "Zurin",
]

female = [
    "Acacia",
    "Adda",
    "Adrasteia",
    "Amaryllis",
    "Amphirite",
    "April",
    "Anna",
    "Arabella",
    "Alenia",
    "Andromache",
    "Antiope",
    "Arethusa",
    "Aria",
    "Arlen",
    "Athena",
    "Audrey",
    "Aurelia",
    "Aurora",
    "Axioche",
    "Azura",
    "Ava",
    "Avalon",
    "Barbarella",
    "Barenziah",
    "Beatrice",
    "Belit",
    "Bianca",
    "Blossom",
    "Bodhmall",
    "Brianne",
    "Bridget",
    "Brooke",
    "Caitlyn",
    "Celes",
    "Camelia",
    "Camilla",
    "Carmen",
    "Casca",
    "Cassima",
    "Cayce",
    "Celeste",
    "Cereza",
    "Charlotte",
    "Cheree",
    "Chevette",
    "Ciri",
    "Cirilla",
    "Cleo",
    "Cleodora",
    "Cleopatra",
    "Dahlia",
    "Dapnhe",
    "Deichtine",
    "Delilah",
    "Delphine",
    "Demeter",
    "Desdemona",
    "Diana",
    "Eir",
    "Eirwen",
    "Electra",
    "Elena",
    "Elisif",
    "Eliza",
    "Emer",
    "Emilia",
    "Erica",
    "Ezra",
    "Esmerelda",
    "Esti",
    "Eve",
    "Fade",
    "Fern",
    "Fiona",
    "Florence",
    "Flynne",
    "Frances",
    "Freya",
    "Gabrielle",
    "Genevieve",
    "Gillian",
    "Gloria",
    "Goneril",
    "Grace",
    "Gwen",
    "Haifa",
    "Heather",
    "Hecuba",
    "Hecate",
    "Harper",
    "Heidrun",
    "Hilary",
    "Hinata",
    "Hollis",
    "Hope",
    "Ida",
    "Igraine",
    "Iman",
    "Ingrid",
    "Iphigeneia",
    "Ira",
    "Irina",
    "Iris",
    "Isabella",
    "Isolde",
    "Ivy",
    "Jaclyn",
    "Janet",
    "Jayne",
    "Jasmine",
    "Jeanne",
    "Jennifer",
    "Jolyne",
    "Juliet",
    "Kalliope",
    "Kara",
    "Katarina",
    "Kei",
    "Kendall",
    "Kendra",
    "Kestrel",
    "Kiyoko",
    "Kira",
    "Keira",
    "Kumiko",
    "Kyra",
    "Lana",
    "Lavender",
    "Laverne",
    "Lavinia",
    "Leia",
    "Leigh",
    "Leuce",
    "Lexi",
    "Libby",
    "Lily",
    "Lilvani",
    "Linda Lee",
    "Lisa",
    "Lola",
    "Lolita",
    "Lolotte",
    "Lucy",
    "Lucille",
    "Luna",
    "Lydia",
    "Mab",
    "Mabel",
    "Marigold",
    "Maeve",
    "Magdalena",
    "Maleficent",
    "Mallory",
    "Malvina",
    "Mary",
    "Maria",
    "Maya",
    "Megha",
    "Melitele",
    "Mephala",
    "Michiko",
    "Minerva",
    "Miranda",
    "Mitsuko",
    "Molly",
    "Moana",
    "Mona",
    "Monika",
    "Morgana",
    "Morticia",
    "Nadia",
    "Narcissa",
    "Nia",
    "Naomi",
    "Noriko",
    "Nulfaga",
    "Nyx",
    "Odette",
    "Ophelia",
    "Olive",
    "Olivia",
    "Olwen",
    "Opal",
    "Orchid",
    "Paetra",
    "Paige",
    "Patricia",
    "Pauline",
    "Pearl",
    "Pepper",
    "Phaedra",
    "Phoebe",
    "Polly Jean",
    "Potema",
    "Quelana",
    "Quinn",
    "Quirina",
    "Rachna",
    "Rachel",
    "Rada",
    "Raina",
    "Rasha",
    "Regan",
    "Regina",
    "Renee",
    "Rhea",
    "Rhianon",
    "Rhys",
    "Ria",
    "Rosa",
    "Rosalind",
    "Rosaria",
    "Rosario",
    "Rose",
    "Rosella",
    "Ruby",
    "Sabrina",
    "Sakura",
    "Samantha",
    "Sansa",
    "Sara",
    "Scarlet",
    "Scarlett",
    "Scheherazade",
    "Scully",
    "Scylla",
    "Senua",
    "Serafina",
    "Sophia",
    "Sibyl",
    "Sif",
    "Sigrun",
    "Simone",
    "Six",
    "Sonja",
    "Skyy",
    "Stella",
    "Suki",
    "Summer",
    "Tamara",
    "Tamiko",
    "Tara",
    "Thalia",
    "Themis",
    "Triss",
    "Ume",
    "Undine",
    "Unice",
    "Valencia",
    "Valeriya",
    "Vee",
    "Vena",
    "Velka",
    "Veronica",
    "Viola",
    "Violet",
    "Vylette",
    "Wednesday",
    "Winona",
    "Wiola",
    "Wynter",
    "Xandra",
    "Xochitl",
    "Xiu",
    "Yana",
    "Yennefer",
    "Ylva",
    "Yoko",
    "Yuan-Xiao",
    "Yuki",
    "Yuria",
    "Zahara",
    "Zelda",
    "Zoe",
]

neuter = [
    "Addison",
    "Anri",
    "Ash",
    "Bishop",
    "Blackthorn",
    "Blake",
    "Blue",
    "Caelan",
    "Dana",
    "Drew",
    "Ghost",
    "Hayden",
    "Hunter",
    "Jones",
    "Justice",
    "Parker",
    "Lane",
    "Mac",
    "Morgan",
    "Oakley",
    "Phoenix",
    "Quinn",
    "Raven",
    "Red",
    "Reese",
    "Revan",
    "Robin",
    "Roan",
    "Sage",
    "Scout",
    "Shadow",
    "Shannon",
    "Starbuck",
    "Storm",
    "Toto",
    "Thorne",
    "Winter",
    "Wolf",
]

