from flask import Flask

from helper import pets

app = Flask(__name__)


@app.route('/')
def index():
  """Returns the HTML content for the index page.

  Returns:
      str: The HTML content for the index page.
  """
  return '''
  <h1>Adopt a Pet!</h1>
  <p>Browse through the links below to find your new furry friend:</p>
  <ul>
    <li>
      <a href="/dogs">Dogs</a>
    </li>
    <li>
    <a href="/cats">Cats</a>
    </li>
    <li>
      <a href="/horses">Horses</a>
    </li>
  </ul>
  '''


listofdogs = pets.get("dogs", "cant find dogs")
first_dog = listofdogs[0]
print(first_dog['name'])
name_of_first_dog = first_dog.get("name", "cant find name")
print(name_of_first_dog)


@app.route('/animals')
def animals():
  html = "<h1>List of pets</h1>"
  for i in pets:
    list_of_dogs = pets.get("dogs")
    list_of_cats = pets.get("cats")
    list_of_rabbits = pets.get("rabbits")
    print(list_of_dogs, list_of_cats, list_of_rabbits)
  return html


@app.route('/animals/<string:pet_type>')
def animals_list(pet_type):
  html = f"<h1>List of {pet_type}"
  return html


@app.route('/dogs')
def dogs():
  return '''What is Lorem Ipsum?
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

Why do we use it?
It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).


Where does it come from?
Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.

The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.

Where can I get some?
There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.'''


@app.route('/cats')
def cats():
  return '''
  cat

  Artikel
  Diskussion
  Läs
  Redigera
  Redigera wikitext
  Visa historik

  Verktyg

  För andra betydelser, se Cat (olika betydelser).
  cat[1] är ett Unixverktyg och kommando som utvecklades i början av 1970-talet.[2] Namnet är kortform för det engelska ordet concatenate som betyder sammanfoga.

  cat har flera användningsområden. De huvudsakliga är att sammanfoga innehållet i filer och att läsa innehållet i filer.[1] Ett ytterligare användningsområde är att skriva en ny textfil.[3] Detta är lämpligt om det avsedda innehållet är mycket enkelt eller i en del mycket speciella situationer, annars är textredigerare som vi bättre.

  Ett relaterad kommando i äldre Microsoft- och DOS-baserade operativsystem är type.[4]
  '''


#STOP


@app.route('/horses')
def horses():
  return '''
  From Wikipedia, the free encyclopedia
  For other uses, see Horse (disambiguation).
  Horse
  Two Nokota horses standing in open grassland with rolling hills and trees visible in the background.
  Conservation status
  Domesticated
  Scientific classificationEdit this classification
  Domain:	Eukaryota
  Kingdom:	Animalia
  Phylum:	Chordata
  Class:	Mammalia
  Order:	Perissodactyla
  Family:	Equidae
  Genus:	Equus
  Species:	E. ferus
  Subspecies:	E. f. caballus
  Trinomial name
  Equus ferus caballus
  Linnaeus, 1758[1]
  Synonyms[2]
  at least 48 published

  The horse (Equus caballus)[2][3] is a domesticated, one-toed, hoofed mammal. It belongs to the taxonomic family Equidae and is one of two extant subspecies of Equus ferus. The horse has evolved over the past 45 to 55 million years from a small multi-toed creature, close to Eohippus, into the large, single-toed animal of today. Humans began domesticating horses around 4000 BCE, and their domestication is believed to have been widespread by 3000 BCE. Horses in the subspecies caballus are domesticated, although some domesticated populations live in the wild as feral horses. These feral populations are not true wild horses, which are horses that never have been domesticated. There is an extensive, specialized vocabulary used to describe equine-related concepts, covering everything from anatomy to life stages, size, colors, markings, breeds, locomotion, and behavior.

  Horses are adapted to run, allowing them to quickly escape predators, and possess an excellent sense of balance and a strong fight-or-flight response. Related to this need to flee from predators in the wild is an unusual trait: horses are able to sleep both standing up and lying down, with younger horses tending to sleep significantly more than adults.[4] Female horses, called mares, carry their young for approximately 11 months and a young horse, called a foal, can stand and run shortly following birth. Most domesticated horses begin training under a saddle or in a harness between the ages of two and four. They reach full adult development by age five, and have an average lifespan of between 25 and 30 years.

  Horse breeds are loosely divided into three categories based on general temperament: spirited "hot bloods" with speed and endurance; "cold bloods", such as draft horses and some ponies, suitable for slow, heavy work; and "warmbloods", developed from crosses between hot bloods and cold bloods, often focusing on creating breeds for specific riding purposes, particularly in Europe. There are more than 300 breeds of horse in the world today, developed for many different uses.

  Horses and humans interact in a wide variety of sport competitions and non-competitive recreational pursuits as well as in working activities such as police work, agriculture, entertainment, and therapy. Horses were historically used in warfare, from which a wide variety of riding and driving techniques developed, using many different styles of equipment and methods of control. Many products are derived from horses, including meat, milk, hide, hair, bone, and pharmaceuticals extracted from the urine of pregnant mares. Humans provide domesticated horses with food, water, and shelter, as well as attention from specialists such as veterinarians and farriers.

  Biology
  Main article: Equine anatomy
  Diagram of a horse with some parts labeled.
  Points of a horse[5][6]
  Specific terms and specialized language are used to describe equine anatomy, different life stages, colors, and breeds.

  Lifespan and life stages
  Depending on breed, management and environment, the modern domestic horse has a life expectancy of 25 to 30 years.[7] Uncommonly, a few animals live into their 40s and, occasionally, beyond.[8] The oldest verifiable record was "Old Billy", a 19th-century horse that lived to the age of 62.[7] In modern times, Sugar Puff, who had been listed in Guinness World Records as the world's oldest living pony, died in 2007 at age 56.[9]

  Regardless of a horse or pony's actual birth date, for most competition purposes a year is added to its age each January 1 of each year in the Northern Hemisphere[7][10] and each August 1 in the Southern Hemisphere.[11] The exception is in endurance riding, where the minimum age to compete is based on the animal's actual calendar age.[12]

  The following terminology is used to describe horses of various ages:

  Foal
  A horse of either sex less than one year old. A nursing foal is sometimes called a suckling, and a foal that has been weaned is called a weanling.[13] Most domesticated foals are weaned at five to seven months of age, although foals can be weaned at four months with no adverse physical effects.[14]
  Yearling
  A horse of either sex that is between one and two years old.[15]
  Colt
  A male horse under the age of four.[16] A common terminology error is to call any young horse a "colt", when the term actually only refers to young male horses.[17]
  Filly
  A female horse under the age of four.[13]
  Mare
  A female horse four years old and older.[18]
  Stallion
  A non-castrated male horse four years old and older.[19] The term "horse" is sometimes used colloquially to refer specifically to a stallion.[20]
  Gelding
  A castrated male horse of any age.[13]
  In horse racing, these definitions may differ: For example, in the British Isles, Thoroughbred horse racing defines colts and fillies as less than five years old.[21] However, Australian Thoroughbred racing defines colts and fillies as less than four years old.[22]

  Size and measurement
  The height of horses is measured at the highest point of the withers, where the neck meets the back.[23] This point is used because it is a stable point of the anatomy, unlike the head or neck, which move up and down in relation to the body of the horse.

  A large brown horse is chasing a small horse in a pasture.
  Size varies greatly among horse breeds, as with this full-sized horse and small pony.
  In English-speaking countries, the height of horses is often stated in units of hands and inches: one hand is equal to 4 inches (101.6 mm). The height is expressed as the number of full hands, followed by a point, then the number of additional inches, and ending with the abbreviation "h" or "hh" (for "hands high"). Thus, a horse described as "15.2 h" is 15 hands plus 2 inches, for a total of 62 inches (157.5 cm) in height.[24]

  The size of horses varies by breed, but also is influenced by nutrition. Light-riding horses usually range in height from 14 to 16 hands (56 to 64 inches, 142 to 163 cm) and can weigh from 380 to 550 kilograms (840 to 1,210 lb).[25] Larger-riding horses usually start at about 15.2 hands (62 inches, 157 cm) and often are as tall as 17 hands (68 inches, 173 cm), weighing from 500 to 600 kilograms (1,100 to 1,320 lb).[26] Heavy or draft horses are usually at least 16 hands (64 inches, 163 cm) high and can be as tall as 18 hands (72 inches, 183 cm) high. They can weigh from about 700 to 1,000 kilograms (1,540 to 2,200 lb).[27]

  The largest horse in recorded history was probably a Shire horse named Mammoth, who was born in 1848. He stood 21.2 1⁄4 hands (86.25 inches, 219 cm) high and his peak weight was estimated at 1,524 kilograms (3,360 lb).[28] The record holder for the smallest horse ever is Thumbelina, a fully mature miniature horse affected by dwarfism. She was 43 centimetres; 4.1 hands (17 in) tall and weighed 26 kg (57 lb).[29][30]

  Ponies
  Main article: Pony
  Ponies are taxonomically the same animals as horses. The distinction between a horse and pony is commonly drawn on the basis of height, especially for competition purposes. However, height alone is not dispositive; the difference between horses and ponies may also include aspects of phenotype, including conformation and temperament.

  The traditional standard for height of a horse or a pony at maturity is 14.2 hands (58 inches, 147 cm). An animal 14.2 hands (58 inches, 147 cm) or over is usually considered to be a horse and one less than 14.2 hands (58 inches, 147 cm) a pony,[31] but there are many exceptions to the traditional standard. In Australia, ponies are considered to be those under 14 hands (56 inches, 142 cm).[32] For competition in the Western division of the United States Equestrian Federation, the cutoff is 14.1 hands (57 inches, 145 cm).[33] The International Federation for Equestrian Sports, the world governing body for horse sport, uses metric measurements and defines a pony as being any horse measuring less than 148 centimetres (58.27 in) at the withers without shoes, which is just over 14.2 hands (58 inches, 147 cm), and 149 centimetres (58.66 in; 14.2+1⁄2 hands), with shoes.[34]

  Height is not the sole criterion for distinguishing horses from ponies. Breed registries for horses that typically produce individuals both under and over 14.2 hands (58 inches, 147 cm) consider all animals of that breed to be horses regardless of their height.[35] Conversely, some pony breeds may have features in common with horses, and individual animals may occasionally mature at over 14.2 hands (58 inches, 147 cm), but are still considered to be ponies.[36]

  Ponies often exhibit thicker manes, tails, and overall coat. They also have proportionally shorter legs, wider barrels, heavier bone, shorter and thicker necks, and short heads with broad foreheads. They may have calmer temperaments than horses and also a high level of intelligence that may or may not be used to cooperate with human handlers.[31] Small size, by itself, is not an exclusive determinant. For example, the Shetland pony which averages 10 hands (40 inches, 102 cm), is considered a pony.[31] Conversely, breeds such as the Falabella and other miniature horses, which can be no taller than 76 centimetres; 7.2 hands (30 in), are classified by their registries as very small horses, not ponies.[37]

  Genetics
  Horses have 64 chromosomes.[38] The horse genome was sequenced in 2007. It contains 2.7 billion DNA base pairs,[39] which is larger than the dog genome, but smaller than the human genome or the bovine genome.[40] The map is available to researchers.[41]

  Colors and markings
  Two horses in a field. The one on the left is a dark brown with a black mane and tail. The one on the right is a light red all over.
  Bay (left) and chestnut (sometimes called "sorrel") are two of the most common coat colors, seen in almost all breeds.
  Main articles: Equine coat color, Equine coat color genetics, and Horse markings
  Horses exhibit a diverse array of coat colors and distinctive markings, described by a specialized vocabulary. Often, a horse is classified first by its coat color, before breed or sex.[42] Horses of the same color may be distinguished from one another by white markings,[43] which, along with various spotting patterns, are inherited separately from coat color.[44]

  Many genes that create horse coat colors and patterns have been identified. Current genetic tests can identify at least 13 different alleles influencing coat color,[45] and research continues to discover new genes linked to specific traits. The basic coat colors of chestnut and black are determined by the gene controlled by the Melanocortin 1 receptor,[46] also known as the "extension gene" or "red factor",[45] as its recessive form is "red" (chestnut) and its dominant form is black.[47] Additional genes control suppression of black color to point coloration that results in a bay, spotting patterns such as pinto or leopard, dilution genes such as palomino or dun, as well as greying, and all the other factors that create the many possible coat colors found in horses.[45]

  Horses that have a white coat color are often mislabeled; a horse that looks "white" is usually a middle-aged or older gray. Grays are born a darker shade, get lighter as they age, but usually keep black skin underneath their white hair coat (with the exception of pink skin under white markings). The only horses properly called white are born with a predominantly white hair coat and pink skin, a fairly rare occurrence.[47] Different and unrelated genetic factors can produce white coat colors in horses, including several different alleles of dominant white and the sabino-1 gene.[48] However, there are no "albino" horses, defined as having both pink skin and red eyes.[49]

  Reproduction and development
  Main article: Horse breeding

  Mare with a foal
  Gestation lasts approximately 340 days, with an average range 320–370 days,[50][51] and usually results in one foal; twins are rare.[52] Horses are a precocial species, and foals are capable of standing and running within a short time following birth.[53] Foals are usually born in the spring. The estrous cycle of a mare occurs roughly every 19–22 days and occurs from early spring into autumn. Most mares enter an anestrus period during the winter and thus do not cycle in this period.[54] Foals are generally weaned from their mothers between four and six months of age.[55]

  Horses, particularly colts, are sometimes physically capable of reproduction at about 18 months, but domesticated horses are rarely allowed to breed before the age of three, especially females.[56] Horses four years old are considered mature, although the skeleton normally continues to develop until the age of six; maturation also depends on the horse's size, breed, sex, and quality of care. Larger horses have larger bones; therefore, not only do the bones take longer to form bone tissue, but the epiphyseal plates are larger and take longer to convert from cartilage to bone. These plates convert after the other parts of the bones, and are crucial to development.[57]

  Depending on maturity, breed, and work expected, horses are usually put under saddle and trained to be ridden between the ages of two and four.[58] Although Thoroughbred race horses are put on the track as young as the age of two in some countries,[59] horses specifically bred for sports such as dressage are generally not put under saddle until they are three or four years old, because their bones and muscles are not solidly developed.[60] For endurance riding competition, horses are not deemed mature enough to compete until they are a full 60 calendar months (five years) old.[12]

  Anatomy
  Main articles: Equine anatomy, Muscular system of the horse, Respiratory system of the horse, and Circulatory system of the horse
  Skeletal system
  Main article: Skeletal system of the horse
  Diagram of a horse skeleton with major parts labeled.
  The skeletal system of a modern horse
  The horse skeleton averages 205 bones.[61] A significant difference between the horse skeleton and that of a human is the lack of a collarbone—the horse's forelimbs are attached to the spinal column by a powerful set of muscles, tendons, and ligaments that attach the shoulder blade to the torso. The horse's four legs and hooves are also unique structures. Their leg bones are proportioned differently from those of a human. For example, the body part that is called a horse's "knee" is actually made up of the carpal bones that correspond to the human wrist. Similarly, the hock contains bones equivalent to those in the human ankle and heel. The lower leg bones of a horse correspond to the bones of the human hand or foot, and the fetlock (incorrectly called the "ankle") is actually the proximal sesamoid bones between the cannon bones (a single equivalent to the human metacarpal or metatarsal bones) and the proximal phalanges, located where one finds the "knuckles" of a human. A horse also has no muscles in its legs below the knees and hocks, only skin, hair, bone, tendons, ligaments, cartilage, and the assorted specialized tissues that make up the hoof.[62]

  Hooves
  Main articles: Horse hoof, Horseshoe, and Farrier
  The critical importance of the feet and legs is summed up by the traditional adage, "no foot, no horse".[63] The horse hoof begins with the distal phalanges, the equivalent of the human fingertip or tip of the toe, surrounded by cartilage and other specialized, blood-rich soft tissues such as the laminae. The exterior hoof wall and horn of the sole is made of keratin, the same material as a human fingernail.[64] The result is that a horse, weighing on average 500 kilograms (1,100 lb),[65] travels on the same bones as would a human on tiptoe.[66] For the protection of the hoof under certain conditions, some horses have horseshoes placed on their feet by a professional farrier. The hoof continually grows, and in most domesticated horses needs to be trimmed (and horseshoes reset, if used) every five to eight weeks,[67] though the hooves of horses in the wild wear down and regrow at a rate suitable for their terrain.

  Teeth
  Main article: Horse teeth
  Horses are adapted to grazing. In an adult horse, there are 12 incisors at the front of the mouth, adapted to biting off the grass or other vegetation. There are 24 teeth adapted for chewing, the premolars and molars, at the back of the mouth. Stallions and geldings have four additional teeth just behind the incisors, a type of canine teeth called "tushes". Some horses, both male and female, will also develop one to four very small vestigial teeth in front of the molars, known as "wolf" teeth, which are generally removed because they can interfere with the bit. There is an empty interdental space between the incisors and the molars where the bit rests directly on the gums, or "bars" of the horse's mouth when the horse is bridled.[68]

  An estimate of a horse's age can be made from looking at its teeth. The teeth continue to erupt throughout life and are worn down by grazing. Therefore, the incisors show changes as the horse ages; they develop a distinct wear pattern, changes in tooth shape, and changes in the angle at which the chewing surfaces meet. This allows a very rough estimate of a horse's age, although diet and veterinary care can also affect the rate of tooth wear.[7]

  Digestion
  Main articles: Equine digestive system and Equine nutrition
  Horses are herbivores with a digestive system adapted to a forage diet of grasses and other plant material, consumed steadily throughout the day. Therefore, compared to humans, they have a relatively small stomach but very long intestines to facilitate a steady flow of nutrients. A 450-kilogram (990 lb) horse will eat 7 to 11 kilograms (15 to 24 lb) of food per day and, under normal use, drink 38 to 45 litres (8.4 to 9.9 imp gal; 10 to 12 US gal) of water. Horses are not ruminants, they have only one stomach, like humans, but unlike humans, they can digest cellulose, a major component of grass. Horses are hindgut fermenters. Cellulose fermentation by symbiotic bacteria occurs in the cecum, or "water gut", which food goes through before reaching the large intestine. Horses cannot vomit, so digestion problems can quickly cause colic, a leading cause of death.[69] Horses do not have a gallbladder; however, they seem to tolerate high amounts of fat in their diet despite lack of a gallbladder.[70][71]

  Senses
  Close up of a horse eye, which is dark brown with lashes on the top eyelid
  A horse's eye
  See also: Equine vision
  The horses' senses are based on their status as prey animals, where they must be aware of their surroundings at all times.[72] They have the largest eyes of any land mammal,[73] and are lateral-eyed, meaning that their eyes are positioned on the sides of their heads.[74] This means that horses have a range of vision of more than 350°, with approximately 65° of this being binocular vision and the remaining 285° monocular vision.[73] Horses have excellent day and night vision, but they have two-color, or dichromatic vision; their color vision is somewhat like red-green color blindness in humans, where certain colors, especially red and related colors, appear as a shade of green.[75]

  Their sense of smell, while much better than that of humans, is not quite as good as that of a dog. It is believed to play a key role in the social interactions of horses as well as detecting other key scents in the environment. Horses have two olfactory centers. The first system is in the nostrils and nasal cavity, which analyze a wide range of odors. The second, located under the nasal cavity, are the vomeronasal organs, also called Jacobson's organs. These have a separate nerve pathway to the brain and appear to primarily analyze pheromones.[76]

  A horse's hearing is good,[72] and the pinna of each ear can rotate up to 180°, giving the potential for 360° hearing without having to move the head.[77] Noise impacts the behavior of horses and certain kinds of noise may contribute to stress: a 2013 study in the UK indicated that stabled horses were calmest in a quiet setting, or if listening to country or classical music, but displayed signs of nervousness when listening to jazz or rock music. This study also recommended keeping music under a volume of 21 decibels.[78] An Australian study found that stabled racehorses listening to talk radio had a higher rate of gastric ulcers than horses listening to music, and racehorses stabled where a radio was played had a higher overall rate of ulceration than horses stabled where there was no radio playing.[79]

  Horses have a great sense of balance, due partly to their ability to feel their footing and partly to highly developed proprioception—the unconscious sense of where the body and limbs are at all times.[80] A horse's sense of touch is well-developed. The most sensitive areas are around the eyes, ears, and nose.[81] Horses are able to sense contact as subtle as an insect landing anywhere on the body.[82]

  Horses have an advanced sense of taste, which allows them to sort through fodder and choose what they would most like to eat,[83] and their prehensile lips can easily sort even small grains. Horses generally will not eat poisonous plants, however, there are exceptions; horses will occasionally eat toxic amounts of poisonous plants even when there is adequate healthy food.[84]

  Movement
  Main articles: Horse gait, Trot, Canter, and Ambling
  Walk 5–8 km/h (3.1–5.0 mph)
  Walk 5–8 km/h (3.1–5.0 mph)

  Trot 8–13 km/h (5.0–8.1 mph)
  Trot 8–13 km/h (5.0–8.1 mph)

  Pace 8–13 km/h (5.0–8.1 mph)
  Pace 8–13 km/h (5.0–8.1 mph)

  Canter 16–27 km/h (9.9–16.8 mph)
  Canter 16–27 km/h (9.9–16.8 mph)

  Gallop 40–48 km/h (25–30 mph), record: 70.76 km/h (43.97 mph)
  Gallop 40–48 km/h (25–30 mph), record: 70.76 km/h (43.97 mph)
  All horses move naturally with four basic gaits:[85]

  the four-beat walk, which averages 6.4 kilometres per hour (4.0 mph);
  the two-beat trot or jog at 13 to 19 kilometres per hour (8.1 to 11.8 mph) (faster for harness racing horses);
  the canter or lope, a three-beat gait that is 19 to 24 kilometres per hour (12 to 15 mph);
  the gallop, which averages 40 to 48 kilometres per hour (25 to 30 mph),[86] but the world record for a horse galloping over a short, sprint distance is 70.76 kilometres per hour (43.97 mph).[87]
  Besides these basic gaits, some horses perform a two-beat pace, instead of the trot.[88] There also are several four-beat 'ambling' gaits that are approximately the speed of a trot or pace, though smoother to ride. These include the lateral rack, running walk, and tölt as well as the diagonal fox trot.[89] Ambling gaits are often genetic in some breeds, known collectively as gaited horses.[90] These horses replace the trot with one of the ambling gaits.[91]

  Behavior
  Main articles: Horse behavior and Stable vices
  Duration: 3 seconds.0:03
  Horse neigh
  Horses are prey animals with a strong fight-or-flight response. Their first reaction to a threat is to startle and usually flee, although they will stand their ground and defend themselves when flight is impossible or if their young are threatened.[92] They also tend to be curious; when startled, they will often hesitate an instant to ascertain the cause of their fright, and may not always flee from something that they perceive as non-threatening. Most light horse riding breeds were developed for speed, agility, alertness and endurance; natural qualities that extend from their wild ancestors. However, through selective breeding, some breeds of horses are quite docile, particularly certain draft horses.[93]


  Horses fighting as part of herd dominance behaviour
  Horses are herd animals, with a clear hierarchy of rank, led by a dominant individual, usually a mare. They are also social creatures that are able to form companionship attachments to their own species and to other animals, including humans. They communicate in various ways, including vocalizations such as nickering or whinnying, mutual grooming, and body language. Many horses will become difficult to manage if they are isolated, but with training, horses can learn to accept a human as a companion, and thus be comfortable away from other horses.[94] However, when confined with insufficient companionship, exercise, or stimulation, individuals may develop stable vices, an assortment of bad habits, mostly stereotypies of psychological origin, that include wood chewing, wall kicking, "weaving" (rocking back and forth), and other problems.[95]

  Intelligence and learning
  Studies have indicated that horses perform a number of cognitive tasks on a daily basis, meeting mental challenges that include food procurement and identification of individuals within a social system. They also have good spatial discrimination abilities.[96] They are naturally curious and apt to investigate things they have not seen before.[97] Studies have assessed equine intelligence in areas such as problem solving, speed of learning, and memory. Horses excel at simple learning, but also are able to use more advanced cognitive abilities that involve categorization and concept learning. They can learn using habituation, desensitization, classical conditioning, and operant conditioning, and positive and negative reinforcement.[96] One study has indicated that horses can differentiate between "more or less" if the quantity involved is less than four.[98]

  Domesticated horses may face greater mental challenges than wild horses, because they live in artificial environments that prevent instinctive behavior whilst also learning tasks that are not natural.[96] Horses are animals of habit that respond well to regimentation, and respond best when the same routines and techniques are used consistently. One trainer believes that "intelligent" horses are reflections of intelligent trainers who effectively use response conditioning techniques and positive reinforcement to train in the style that best fits with an individual animal's natural inclinations.[99]

  Temperament
  Main articles: Draft horse, Warmblood, Oriental horse, and Hot-blooded horse
  Horses are mammals, and as such are warm-blooded, or endothermic creatures, as opposed to cold-blooded, or poikilothermic animals. However, these words have developed a separate meaning in the context of equine terminology, used to describe temperament, not body temperature. For example, the "hot-bloods", such as many race horses, exhibit more sensitivity and energy,[100] while the "cold-bloods", such as most draft breeds, are quieter and calmer.[101] Sometimes "hot-bloods" are classified as "light horses" or "riding horses",[102] with the "cold-bloods" classified as "draft horses" or "work horses".[103]

  a sepia-toned engraving from an old book, showing 11 horses of different breeds and sizes in nine different illustrations
  Illustration of assorted breeds; slim, light hotbloods, medium-sized warmbloods and draft and pony-type coldblood breeds
  "Hot blooded" breeds include "oriental horses" such as the Akhal-Teke, Arabian horse, Barb, and now-extinct Turkoman horse, as well as the Thoroughbred, a breed developed in England from the older oriental breeds.[100] Hot bloods tend to be spirited, bold, and learn quickly. They are bred for agility and speed.[104] They tend to be physically refined—thin-skinned, slim, and long-legged.[105] The original oriental breeds were brought to Europe from the Middle East and North Africa when European breeders wished to infuse these traits into racing and light cavalry horses.[106][107]

  Muscular, heavy draft horses are known as "cold bloods", as they are bred not only for strength, but also to have the calm, patient temperament needed to pull a plow or a heavy carriage full of people.[101] They are sometimes nicknamed "gentle giants".[108] Well-known draft breeds include the Belgian and the Clydesdale.[108] Some, like the Percheron, are lighter and livelier, developed to pull carriages or to plow large fields in drier climates.[109] Others, such as the Shire, are slower and more powerful, bred to plow fields with heavy, clay-based soils.[110] The cold-blooded group also includes some pony breeds.[111]

  "Warmblood" breeds, such as the Trakehner or Hanoverian, developed when European carriage and war horses were crossed with Arabians or Thoroughbreds, producing a riding horse with more refinement than a draft horse, but greater size and milder temperament than a lighter breed.[112] Certain pony breeds with warmblood characteristics have been developed for smaller riders.[113] Warmbloods are considered a "light horse" or "riding horse".[102]

  Today, the term "Warmblood" refers to a specific subset of sport horse breeds that are used for competition in dressage and show jumping.[114] Strictly speaking, the term "warm blood" refers to any cross between cold-blooded and hot-blooded breeds.[115] Examples include breeds such as the Irish Draught or the Cleveland Bay. The term was once used to refer to breeds of light riding horse other than Thoroughbreds or Arabians, such as the Morgan horse.[104]

  Sleep patterns
  See also: Horse sleep patterns and Sleep in non-humans
  Two horses in a pasture, one is standing beside the other that is laying down.
  When horses lie down to sleep, others in the herd remain standing, awake, or in a light doze, keeping watch.
  Horses are able to sleep both standing up and lying down. In an adaptation from life in the wild, horses are able to enter light sleep by using a "stay apparatus" in their legs, allowing them to doze without collapsing.[116] Horses sleep better when in groups because some animals will sleep while others stand guard to watch for predators. A horse kept alone will not sleep well because its instincts are to keep a constant eye out for danger.[117]

  Unlike humans, horses do not sleep in a solid, unbroken period of time, but take many short periods of rest. Horses spend four to fifteen hours a day in standing rest, and from a few minutes to several hours lying down. Total sleep time in a 24-hour period may range from several minutes to a couple of hours,[117] mostly in short intervals of about 15 minutes each.[118] The average sleep time of a domestic horse is said to be 2.9 hours per day.[119]

  Horses must lie down to reach REM sleep. They only have to lie down for an hour or two every few days to meet their minimum REM sleep requirements.[117] However, if a horse is never allowed to lie down, after several days it will become sleep-deprived, and in rare cases may suddenly collapse as it involuntarily slips into REM sleep while still standing.[120] This condition differs from narcolepsy, although horses may also suffer from that disorder.[121]

  Taxonomy and evolution

  Diagram of evolution in horses showing size development, biometrical changes in the cranium and reduction of toes (left forefoot)
  Main articles: Evolution of the horse, Equus (genus), and Equidae
  The horse adapted to survive in areas of wide-open terrain with sparse vegetation, surviving in an ecosystem where other large grazing animals, especially ruminants, could not.[122] Horses and other equids are odd-toed ungulates of the order Perissodactyla, a group of mammals dominant during the Tertiary period. In the past, this order contained 14 families, but only three—Equidae (the horse and related species), Tapiridae (the tapir), and Rhinocerotidae (the rhinoceroses)—have survived to the present day.[123]

  The earliest known member of the family Equidae was the Hyracotherium, which lived between 45 and 55 million years ago, during the Eocene period. It had 4 toes on each front foot, and 3 toes on each back foot.[124] The extra toe on the front feet soon disappeared with the Mesohippus, which lived 32 to 37 million years ago.[125] Over time, the extra side toes shrank in size until they vanished. All that remains of them in modern horses is a set of small vestigial bones on the leg below the knee,[126] known informally as splint bones.[127] Their legs also lengthened as their toes disappeared until they were a hooved animal capable of running at great speed.[126] By about 5 million years ago, the modern Equus had evolved.[128] Equid teeth also evolved from browsing on soft, tropical plants to adapt to browsing of drier plant material, then to grazing of tougher plains grasses. Thus proto-horses changed from leaf-eating forest-dwellers to grass-eating inhabitants of semi-arid regions worldwide, including the steppes of Eurasia and the Great Plains of North America.

  By about 15,000 years ago, Equus ferus was a widespread holarctic species. Horse bones from this time period, the late Pleistocene, are found in Europe, Eurasia, Beringia, and North America.[129] Yet between 10,000 and 7,600 years ago, the horse became extinct in North America.[130][131][132] The reasons for this extinction are not fully known, but one theory notes that extinction in North America paralleled human arrival.[133] Another theory points to climate change, noting that approximately 12,500 years ago, the grasses characteristic of a steppe ecosystem gave way to shrub tundra, which was covered with unpalatable plants.[134]

  Wild species surviving into modern times
  Three tan-colored horses with upright manes. Two horses nip and paw at each other, while the third moves towards the camera. They stand in an open, rocky grassland, with forests in the distance.
  A small herd of Przewalski's Horses
  Main article: Wild horse
  A truly wild horse is a species or subspecies with no ancestors that were ever successfully domesticated. Therefore, most "wild" horses today are actually feral horses, animals that escaped or were turned loose from domestic herds and the descendants of those animals.[135] Only two wild subspecies, the tarpan and the Przewalski's horse, survived into recorded history and only the latter survives today.

  The Przewalski's horse (Equus ferus przewalskii), named after the Russian explorer Nikolai Przhevalsky, is a rare Asian animal. It is also known as the Mongolian wild horse; Mongolian people know it as the taki, and the Kyrgyz people call it a kirtag. The subspecies was presumed extinct in the wild between 1969 and 1992, while a small breeding population survived in zoos around the world. In 1992, it was reestablished in the wild by the conservation efforts of numerous zoos.[136] Today, a small wild breeding population exists in Mongolia.[137][138] There are additional animals still maintained at zoos throughout the world.

  The question of whether the Przewalski's horse was ever domesticated was challenged in 2018 when DNA studies of horses found at Botai culture sites revealed captured animals with DNA markers of an ancestor to the Przewalski's horse. The study concluded that the Botai animals appear to have been an independent domestication attempt and apparently unsuccessful, as these genetic markers do not appear in modern domesticated horses. However, the question of whether all Przewalski's horses descend from this population is also unresolved, as only one of seven modern Przewalski's horses in the study shared this ancestry.[139][140][141]

  The tarpan or European wild horse (Equus ferus ferus) was found in Europe and much of Asia. It survived into the historical era, but became extinct in 1909, when the last captive died in a Russian zoo.[142] Thus, the genetic line was lost. Attempts have been made to recreate the tarpan,[142][143][144] which resulted in horses with outward physical similarities, but nonetheless descended from domesticated ancestors and not true wild horses.

  Periodically, populations of horses in isolated areas are speculated to be relict populations of wild horses, but generally have been proven to be feral or domestic. For example, the Riwoche horse of Tibet was proposed as such,[138] but testing did not reveal genetic differences from domesticated horses.[145] Similarly, the Sorraia of Portugal was proposed as a direct descendant of the Tarpan on the basis of shared characteristics,[146][147] but genetic studies have shown that the Sorraia is more closely related to other horse breeds, and that the outward similarity is an unreliable measure of relatedness.[146][148]

  Other modern equids
  Main article: Equus (genus)
  Besides the horse, there are six other species of genus Equus in the Equidae family. These are the ass or donkey, Equus asinus; the mountain zebra, Equus zebra; plains zebra, Equus quagga; Grévy's Zebra, Equus grevyi; the kiang, Equus kiang; and the onager, Equus hemionus.[149]

  Horses can crossbreed with other members of their genus. The most common hybrid is the mule, a cross between a "jack" (male donkey) and a mare. A related hybrid, a hinny, is a cross between a stallion and a "jenny" (female donkey).[150] Other hybrids include the zorse, a cross between a zebra and a horse.[151] With rare exceptions, most hybrids are sterile and cannot reproduce.[152]

  Domestication and history
  Main articles: History of horse domestication theories and Domestication of the horse


  Bhimbetka rock painting showing a man riding on a horse, India
  Domestication of the horse most likely took place in central Asia prior to 3500 BCE. Two major sources of information are used to determine where and when the horse was first domesticated and how the domesticated horse spread around the world. The first source is based on palaeological and archaeological discoveries; the second source is a comparison of DNA obtained from modern horses to that from bones and teeth of ancient horse remains.

  The earliest archaeological evidence for the domestication of the horse comes from sites in Ukraine and Kazakhstan, dating to approximately 4000–3500 BCE.[153][154][155] By 3000 BCE, the horse was completely domesticated and by 2000 BCE there was a sharp increase in the number of horse bones found in human settlements in northwestern Europe, indicating the spread of domesticated horses throughout the continent.[156] The most recent, but most irrefutable evidence of domestication comes from sites where horse remains were interred with chariots in graves of the Sintashta and Petrovka cultures c. 2100 BCE.[157]

  A 2021 genetic study suggested that most modern domestic horses descend from the lower Volga-Don region. Ancient horse genomes indicate that these populations influenced almost all local populations as they expanded rapidly throughout Eurasia, beginning about 4,200 years ago. It also shows that certain adaptations were strongly selected due to riding, and that equestrian material culture, including Sintashta spoke-wheeled chariots spread with the horse itself.[158][159]

  Domestication is also studied by using the genetic material of present-day horses and comparing it with the genetic material present in the bones and teeth of horse remains found in archaeological and palaeological excavations. The variation in the genetic material shows that very few wild stallions contributed to the domestic horse,[160][161] while many mares were part of early domesticated herds.[148][162][163] This is reflected in the difference in genetic variation between the DNA that is passed on along the paternal, or sire line (Y-chromosome) versus that passed on along the maternal, or dam line (mitochondrial DNA). There are very low levels of Y-chromosome variability,[160][161] but a great deal of genetic variation in mitochondrial DNA.[148][162][163] There is also regional variation in mitochondrial DNA due to the inclusion of wild mares in domestic herds.[148][162][163][164] Another characteristic of domestication is an increase in coat color variation.[165] In horses, this increased dramatically between 5000 and 3000 BCE.[166]

  Before the availability of DNA techniques to resolve the questions related to the domestication of the horse, various hypotheses were proposed. One classification was based on body types and conformation, suggesting the presence of four basic prototypes that had adapted to their environment prior to domestication.[111] Another hypothesis held that the four prototypes originated from a single wild species and that all different body types were entirely a result of selective breeding after domestication.[167] However, the lack of a detectable substructure in the horse has resulted in a rejection of both hypotheses.

  Feral populations
  Main article: Feral horse
  Feral horses are born and live in the wild, but are descended from domesticated animals.[135] Many populations of feral horses exist throughout the world.[168][169] Studies of feral herds have provided useful insights into the behavior of prehistoric horses,[170] as well as greater understanding of the instincts and behaviors that drive horses that live in domesticated conditions.[171]

  There are also semi-feral horses in many parts of the world, such as Dartmoor and the New Forest in the UK, where the animals are all privately owned but live for significant amounts of time in "wild" conditions on undeveloped, often public, lands. Owners of such animals often pay a fee for grazing rights.[172][173]

  Breeds
  Main articles: Horse breed, List of horse breeds, and Horse breeding
  The concept of purebred bloodstock and a controlled, written breed registry has come to be particularly significant and important in modern times. Sometimes purebred horses are incorrectly or inaccurately called "thoroughbreds". Thoroughbred is a specific breed of horse, while a "purebred" is a horse (or any other animal) with a defined pedigree recognized by a breed registry.[174] Horse breeds are groups of horses with distinctive characteristics that are transmitted consistently to their offspring, such as conformation, color, performance ability, or disposition. These inherited traits result from a combination of natural crosses and artificial selection methods. Horses have been selectively bred since their domestication. An early example of people who practiced selective horse breeding were the Bedouin, who had a reputation for careful practices, keeping extensive pedigrees of their Arabian horses and placing great value upon pure bloodlines.[175] These pedigrees were originally transmitted via an oral tradition.[176] In the 14th century, Carthusian monks of southern Spain kept meticulous pedigrees of bloodstock lineages still found today in the Andalusian horse.[177]

  Breeds developed due to a need for "form to function", the necessity to develop certain characteristics in order to perform a particular type of work.[178] Thus, a powerful but refined breed such as the Andalusian developed as riding horses with an aptitude for dressage.[178] Heavy draft horses were developed out of a need to perform demanding farm work and pull heavy wagons.[179] Other horse breeds had been developed specifically for light agricultural work, carriage and road work, various sport disciplines, or simply as pets.[180] Some breeds developed through centuries of crossing other breeds, while others descended from a single foundation sire, or other limited or restricted foundation bloodstock. One of the earliest formal registries was General Stud Book for Thoroughbreds, which began in 1791 and traced back to the foundation bloodstock for the breed.[181] There are more than 300 horse breeds in the world today.[182]

  Interaction with humans

  Finnhorse pulling a heavy wagon.
  Worldwide, horses play a role within human cultures and have done so for millennia. Horses are used for leisure activities, sports, and working purposes. The Food and Agriculture Organization (FAO) estimates that in 2008, there were almost 59,000,000 horses in the world, with around 33,500,000 in the Americas, 13,800,000 in Asia and 6,300,000 in Europe and smaller portions in Africa and Oceania. There are estimated to be 9,500,000 horses in the United States alone.[183] The American Horse Council estimates that horse-related activities have a direct impact on the economy of the United States of over $39 billion, and when indirect spending is considered, the impact is over $102 billion.[184] In a 2004 "poll" conducted by Animal Planet, more than 50,000 viewers from 73 countries voted for the horse as the world's 4th favorite animal.[185]

  Communication between human and horse is paramount in any equestrian activity;[186] to aid this process horses are usually ridden with a saddle on their backs to assist the rider with balance and positioning, and a bridle or related headgear to assist the rider in maintaining control.[187] Sometimes horses are ridden without a saddle,[188] and occasionally, horses are trained to perform without a bridle or other headgear.[189] Many horses are also driven, which requires a harness, bridle, and some type of vehicle.[190]

  Sport
  A chestnut (reddish-brown) horse being ridden by a rider in a black coat and top hat. They are stopped in a riding arena with the rider tipping his hat.
  A horse and rider in dressage competition at the Olympics
  Main articles: Equestrianism, Horse racing, Horse training, and Horse tack
  Historically, equestrians honed their skills through games and races. Equestrian sports provided entertainment for crowds and honed the excellent horsemanship that was needed in battle. Many sports, such as dressage, eventing, and show jumping, have origins in military training, which were focused on control and balance of both horse and rider. Other sports, such as rodeo, developed from practical skills such as those needed on working ranches and stations. Sport hunting from horseback evolved from earlier practical hunting techniques.[186] Horse racing of all types evolved from impromptu competitions between riders or drivers. All forms of competition, requiring demanding and specialized skills from both horse and rider, resulted in the systematic development of specialized breeds and equipment for each sport. The popularity of equestrian sports through the centuries has resulted in the preservation of skills that would otherwise have disappeared after horses stopped being used in combat.[186]

  Horses are trained to be ridden or driven in a variety of sporting competitions. Examples include show jumping, dressage, three-day eventing, competitive driving, endurance riding, gymkhana, rodeos, and fox hunting.[191] Horse shows, which have their origins in medieval European fairs, are held around the world. They host a huge range of classes, covering all of the mounted and harness disciplines, as well as "In-hand" classes where the horses are led, rather than ridden, to be evaluated on their conformation. The method of judging varies with the discipline, but winning usually depends on style and ability of both horse and rider.[192] Sports such as polo do not judge the horse itself, but rather use the horse as a partner for human competitors as a necessary part of the game. Although the horse requires specialized training to participate, the details of its performance are not judged, only the result of the rider's actions—be it getting a ball through a goal or some other task.[193] Examples of these sports of partnership between human and horse include jousting, in which the main goal is for one rider to unseat the other,[194] and buzkashi, a team game played throughout Central Asia, the aim being to capture a goat carcass while on horseback.[193]

  Horse racing is an equestrian sport and major international industry, watched in almost every nation of the world. There are three types: "flat" racing; steeplechasing, i.e. racing over jumps; and harness racing, where horses trot or pace while pulling a driver in a small, light cart known as a sulky.[195] A major part of horse racing's economic importance lies in the gambling associated with it.[196]

  Work
  Tired-looking bay horse hitched to a rustic cart
  Horse pulling a cart
  A mounted man in a blue uniform on a dark brown horse
  A mounted police officer in Poland
  There are certain jobs that horses do very well, and no technology has yet developed to fully replace them. For example, mounted police horses are still effective for certain types of patrol duties and crowd control.[197] Cattle ranches still require riders on horseback to round up cattle that are scattered across remote, rugged terrain.[198] Search and rescue organizations in some countries depend upon mounted teams to locate people, particularly hikers and children, and to provide disaster relief assistance.[199] Horses can also be used in areas where it is necessary to avoid vehicular disruption to delicate soil, such as nature reserves. They may also be the only form of transport allowed in wilderness areas. Horses are quieter than motorized vehicles. Law enforcement officers such as park rangers or game wardens may use horses for patrols, and horses or mules may also be used for clearing trails or other work in areas of rough terrain where vehicles are less effective.[200]

  Although machinery has replaced horses in many parts of the world, an estimated 100 million horses, donkeys and mules are still used for agriculture and transportation in less developed areas. This number includes around 27 million working animals in Africa alone.[201] Some land management practices such as cultivating and logging can be efficiently performed with horses. In agriculture, less fossil fuel is used and increased environmental conservation occurs over time with the use of draft animals such as horses.[202][203] Logging with horses can result in reduced damage to soil structure and less damage to trees due to more selective logging.[204]

  Warfare
  Main article: Horses in warfare
  Black-and-white photo of mounted soldiers with middle eastern headwraps, carrying rifles, walking down a road away from the camera
  Ottoman cavalry, 1917
  Horses have been used in warfare for most of recorded history. The first archaeological evidence of horses used in warfare dates to between 4000 and 3000 BCE,[205] and the use of horses in warfare was widespread by the end of the Bronze Age.[206][207] Although mechanization has largely replaced the horse as a weapon of war, horses are still seen today in limited military uses, mostly for ceremonial purposes, or for reconnaissance and transport activities in areas of rough terrain where motorized vehicles are ineffective. Horses have been used in the 21st century by the Janjaweed militias in the War in Darfur.[208]

  Entertainment and culture

  The horse-headed deity in Hinduism, Hayagriva
  See also: Horse symbolism, Horses in art, and Horse worship
  Modern horses are often used to reenact many of their historical work purposes. Horses are used, complete with equipment that is authentic or a meticulously recreated replica, in various live action historical reenactments of specific periods of history, especially recreations of famous battles.[209] Horses are also used to preserve cultural traditions and for ceremonial purposes. Countries such as the United Kingdom still use horse-drawn carriages to convey royalty and other VIPs to and from certain culturally significant events.[210] Public exhibitions are another example, such as the Budweiser Clydesdales, seen in parades and other public settings, a team of draft horses that pull a beer wagon similar to that used before the invention of the modern motorized truck.[211]

  Horses are frequently used in television, films and literature. They are sometimes featured as a major character in films about particular animals, but also used as visual elements that assure the accuracy of historical stories.[212] Both live horses and iconic images of horses are used in advertising to promote a variety of products.[213] The horse frequently appears in coats of arms in heraldry, in a variety of poses and equipment.[214] The mythologies of many cultures, including Greco-Roman, Hindu, Islamic, and Germanic, include references to both normal horses and those with wings or additional limbs, and multiple myths also call upon the horse to draw the chariots of the Moon and Sun.[215] The horse also appears in the 12-year cycle of animals in the Chinese zodiac related to the Chinese calendar.[216]

  Horses serve as the inspiration for many modern automobile names and logos, including the Ford Pinto, Ford Bronco, Ford Mustang, Hyundai Equus, Hyundai Pony, Mitsubishi Starion, Subaru Brumby, Mitsubishi Colt/Dodge Colt, Pinzgauer, Steyr-Puch Haflinger, Pegaso, Porsche, Rolls-Royce Camargue, Ferrari, Carlsson, Kamaz, Corre La Licorne, Iran Khodro, Eicher, and Baojun.[217][218][219] Indian TVS Motor Company also uses a horse on their motorcycles & scooters.

  Therapeutic use
  See also: Equine-assisted therapy and Therapeutic horseback riding
  People of all ages with physical and mental disabilities obtain beneficial results from an association with horses. Therapeutic riding is used to mentally and physically stimulate disabled persons and help them improve their lives through improved balance and coordination, increased self-confidence, and a greater feeling of freedom and independence.[220] The benefits of equestrian activity for people with disabilities has also been recognized with the addition of equestrian events to the Paralympic Games and recognition of para-equestrian events by the International Federation for Equestrian Sports (FEI).[221] Hippotherapy and therapeutic horseback riding are names for different physical, occupational, and speech therapy treatment strategies that use equine movement. In hippotherapy, a therapist uses the horse's movement to improve their patient's cognitive, coordination, balance, and fine motor skills, whereas therapeutic horseback riding uses specific riding skills.[222]

  Horses also provide psychological benefits to people whether they actually ride or not. "Equine-assisted" or "equine-facilitated" therapy is a form of experiential psychotherapy that uses horses as companion animals to assist people with mental illness, including anxiety disorders, psychotic disorders, mood disorders, behavioral difficulties, and those who are going through major life changes.[223] There are also experimental programs using horses in prison settings. Exposure to horses appears to improve the behavior of inmates and help reduce recidivism when they leave.[224]

  Products
  Horses are raw material for many products made by humans throughout history, including byproducts from the slaughter of horses as well as materials collected from living horses.

  Products collected from living horses include mare's milk, used by people with large horse herds, such as the Mongols, who let it ferment to produce kumis.[225] Horse blood was once used as food by the Mongols and other nomadic tribes, who found it a convenient source of nutrition when traveling. Drinking their own horses' blood allowed the Mongols to ride for extended periods of time without stopping to eat.[225] The drug Premarin is a mixture of estrogens extracted from the urine of pregnant mares (pregnant mares' urine), and was previously a widely used drug for hormone replacement therapy.[226] The tail hair of horses can be used for making bows for string instruments such as the violin, viola, cello, and double bass.[227]

  Horse meat has been used as food for humans and carnivorous animals throughout the ages. Approximately 5 million horses are slaughtered each year for meat worldwide.[228] It is eaten in many parts of the world, though consumption is taboo in some cultures,[229] and a subject of political controversy in others.[230] Horsehide leather has been used for boots, gloves, jackets,[231] baseballs,[232] and baseball gloves. Horse hooves can also be used to produce animal glue.[233] Horse bones can be used to make implements.[234] Specifically, in Italian cuisine, the horse tibia is sharpened into a probe called a spinto, which is used to test the readiness of a (pig) ham as it cures.[235] In Asia, the saba is a horsehide vessel used in the production of kumis.[236]

  Care
  Main article: Horse care
  See also: Equine nutrition, Horse grooming, Veterinary medicine, and Farrier
  A young man in US military clothing examines the teeth of a bay (dark brown) horse, while another person in military work clothing, partially obscured, holds the horse. Several other people are partially visible in the background.
  Checking teeth and other physical examinations are an important part of horse care.
  Horses are grazing animals, and their major source of nutrients is good-quality forage from hay or pasture.[237] They can consume approximately 2% to 2.5% of their body weight in dry feed each day. Therefore, a 450-kilogram (990 lb) adult horse could eat up to 11 kilograms (24 lb) of food.[238] Sometimes, concentrated feed such as grain is fed in addition to pasture or hay, especially when the animal is very active.[239] When grain is fed, equine nutritionists recommend that 50% or more of the animal's diet by weight should still be forage.[240]

  Horses require a plentiful supply of clean water, a minimum of 38 to 45 litres (10 to 12 US gal) per day.[241] Although horses are adapted to live outside, they require shelter from the wind and precipitation, which can range from a simple shed or shelter to an elaborate stable.[242]

  Horses require routine hoof care from a farrier, as well as vaccinations to protect against various diseases, and dental examinations from a veterinarian or a specialized equine dentist.[243] If horses are kept inside in a barn, they require regular daily exercise for their physical health and mental well-being.[244] When turned outside, they require well-maintained, sturdy fences to be safely contained.[245] Regular grooming is also helpful to help the horse maintain good health of the hair coat and underlying skin.[246]

  Climate change
  This section is an excerpt from Effects of climate change on livestock § Equines.[edit]

  Diagram of heat regulation in horses.[247]
  As of 2019, there are around 17 million horses in the world. Healthy body temperature for adult horses is in the range between 37.5 and 38.5 °C (99.5 and 101.3 °F), which they can maintain while ambient temperatures are between 5 and 25 °C (41 and 77 °F). However, strenuous exercise increases core body temperature by 1 °C (1.8 °F)/minute, as 80% of the energy used by equine muscles is released as heat. Along with bovines and primates, equines are the only animal group which use sweating as their primary method of thermoregulation: in fact, it can account for up to 70% of their heat loss, and horses sweat three times more than humans while undergoing comparably strenuous physical activity. Unlike humans, this sweat is created not by eccrine glands but by apocrine glands.[248] In hot conditions, horses during three hours of moderate-intersity exercise can loss 30 to 35 L of water and 100g of sodium, 198 g of choloride and 45 g of potassium.[248] In another difference from humans, their sweat is hypertonic, and contains a protein called latherin,[249] which enables it to spread across their body easier, and to foam, rather than to drip off. These adaptations are partly to compensate for their lower body surface-to-mass ratio, which makes it more difficult for horses to passively radiate heat. Yet, prolonged exposure to very hot and/or humid conditions will lead to consequences such as anhidrosis, heat stroke, or brain damage, potentially culminating in death if not addressed with measures like cold water applications. Additionally, around 10% of incidents associated with horse transport have been attributed to heat stress. These issues are expected to worsen in the future.[247]

  African horse sickness (AHS) is a viral illness with a mortality close to 90% in horses, and 50% in mules. A midge, Culicoides imicola, is the primary vector of AHS, and its spread is expected to benefit from climate change.[250] The spillover of Hendra virus from its flying fox hosts to horses is also likely to increase, as future warming would expand the hosts' geographic range. It has been estimated that under the "moderate" and high climate change scenarios, RCP4.5 and RCP8.5, the number of threatened horses would increase by 110,000 and 165,000, respectively, or by 175 and 260%.[251]
  See also
  Glossary of equestrian terms
  Lists of horse-related topics
  List of historical horses
  Dülmener
  The horse in Nordic mythology
  Equus gallicus
  Solutré horse
  References
   Linnaeus, Carolus (1758). Systema naturae per regna tria naturae :secundum classes, ordines, genera, species, cum characteribus, differentiis, synonymis, locis. Vol. 1 (10th ed.). Holmiae (Laurentii Salvii). p. 73. Archived from the original on 2018-10-12. Retrieved 2008-09-08.
   Grubb, P. (2005). "Order Perissodactyla". In Wilson, D.E.; Reeder, D.M (eds.). Mammal Species of the World: A Taxonomic and Geographic Reference (3rd ed.). Johns Hopkins University Press. pp. 630–631. ISBN 978-0-8018-8221-0. OCLC 62265494.
   International Commission on Zoological Nomenclature (2003). "Usage of 17 specific names based on wild species which are pre-dated by or contemporary with those based on domestic animals (Lepidoptera, Osteichthyes, Mammalia): conserved. Opinion 2027 (Case 3010)". Bull. Zool. Nomencl. 60 (1): 81–84. Archived from the original on 2007-08-21.
   "Do You Know How Horses Sleep?". Archived from the original on 22 January 2018. Retrieved 12 September 2018.
   Goody, John (2000). Horse Anatomy (2nd ed.). J A Allen. ISBN 0-85131-769-3.
   Pavord, Tony; Pavord, Marcy (2007). Complete Equine Veterinary Manual. David & Charles. ISBN 978-0-7153-1883-6.
   Ensminger, pp. 46–50
   Wright, B. (March 29, 1999). "The Age of a Horse". Ministry of Agriculture, Food and Rural Affairs. Government of Ontario. Archived from the original on January 20, 2010. Retrieved 2009-10-21.
   Ryder, Erin. "World's Oldest Living Pony Dies at 56". The Horse. Archived from the original on 2014-01-24. Retrieved 2007-05-31.
   British Horse Society (1966). The Manual of Horsemanship of the British Horse Society and the Pony Club (6th edition, reprinted 1970 ed.). Kenilworth, UK: British Horse Society. p. 255. ISBN 0-9548863-1-3.
   "Rules of the Australian Stud Book" (PDF). Australian Jockey Club. 2007. p. 7. Archived from the original on 2013-04-24. Retrieved 2008-07-09.
   "Equine Age Requirements for AERC Rides". American Endurance Riding Conference. Archived from the original on 2011-08-11. Retrieved 2011-07-25.
   Ensminger, p. 418
   Giffin, p. 431
   Ensminger, p. 430
   Ensminger, p. 415
   Becker, Marty; Pavia, Audrey; Spadafori, Gina; Becker, Teresa (2007). Why Do Horses Sleep Standing Up?: 101 of the Most Perplexing Questions Answered About Equine Enigmas, Medical Mysteries, and Befuddling Behaviors. HCI. p. 23. ISBN 978-0-7573-0608-2.
   Ensminger, p. 422
   Ensminger, p. 427
   Ensminger, p. 420
   "Glossary of Horse Racing Terms". Equibase.com. Equibase Company, LLC. Archived from the original on 2008-05-12. Retrieved 2008-04-03.
   "Rules of the Australian Stud Book". Australian Jockey Club Ltd and Victoria Racing Club Ltd. July 2008. p. 9. Archived from the original on 2013-04-24. Retrieved 2010-02-05.
   Whitaker, p. 77
   Ensminger, p. 51
   Bongianni, entries 1, 68, 69
   Bongianni, entries 12, 30, 31, 32, 75
   Bongianni, entries 86, 96, 97
   Whitaker, p. 60
   Douglas, Jeff (2007-03-19). "World's smallest horse has tall order". The Washington Post. Associated Press. Archived from the original on 2017-03-15. Retrieved 2017-03-14.
   "Meet the smallest horse in the world that's shorter than a greyhound". Guinness World Records. 2019-09-05. Archived from the original on 2021-08-04. Retrieved 2021-07-06.
   Ensminger, M.E. (1991). Horses and Tack (Revised ed.). Boston, MA: Houghton Mifflin Company. pp. 11–12. ISBN 0395544130. OCLC 21561287.
   Howlett, Lorna; Philip Mathews (1979). Ponies in Australia. Milson's Point, NSW: Philip Mathews Publishers. p. 14. ISBN 0-908001-13-4.
   "2012 United States Equestrian Federation, Inc. Rule Book". United States Equestrian Federation. p. Rule WS 101. Archived from the original on 2012-04-15.
   "Annex XVII: Extracts from Rules for Pony Riders and Children, 9th edition" (PDF). Fédération Equestre Internationale. 2009. Archived from the original (PDF) on 2012-09-11. Retrieved 2010-03-07.
   For example, the Missouri Fox Trotter, or the Arabian horse. See McBane, pp. 192, 218
   For example, the Welsh Pony. See McBane, pp. 52–63
   McBane, p. 200
   "Chromosome Numbers in Different Species". Vivo.colostate.edu. 1998-01-30. Archived from the original on 2013-05-11. Retrieved 2013-04-17.
   "Sequenced horse genome expands understanding of equine, human diseases". Cornell University College of Veterinary Medicine. 2012-08-21. Archived from the original on 2017-10-10. Retrieved 2013-04-01.
   Wade, C. M; Giulotto, E; Sigurdsson, S; Zoli, M; Gnerre, S; Imsland, F; Lear, T. L; Adelson, D. L; Bailey, E; Bellone, R. R; Blocker, H; Distl, O; Edgar, R. C; Garber, M; Leeb, T; Mauceli, E; MacLeod, J. N; Penedo, M. C. T; Raison, J. M; Sharpe, T; Vogel, J; Andersson, L; Antczak, D. F; Biagi, T; Binns, M. M; Chowdhary, B. P; Coleman, S. J; Della Valle, G; Fryc, S; et al. (2009-11-05). "Domestic Horse Genome Sequenced". Science. 326 (5954): 865–867. Bibcode:2009Sci...326..865W. doi:10.1126/science.1178158. PMC 3785132. PMID 19892987. Archived from the original on 2018-11-18. Retrieved 2013-04-01.
   "Ensembl genome browser 71: Equus caballus – Description". Uswest.ensembl.org. Archived from the original on 2017-10-10. Retrieved 2013-04-17.
   Vogel, Colin B.V.M. (1995). The Complete Horse Care Manual. New York: Dorling Kindersley Publishing, Inc. p. 14. ISBN 0-7894-0170-3. OCLC 32168476.
   Mills, Bruce; Barbara Carne (1988). A Basic Guide to Horse Care and Management. New York: Howell Book House. pp. 72–73. ISBN 0-87605-871-3. OCLC 17507227.
   Corum, Stephanie J. (May 1, 2003). "A Horse of a Different Color". The Horse. Archived from the original on 2015-09-18. Retrieved 2010-02-11.
   "Horse Coat Color Tests". Veterinary Genetics Laboratory. University of California. Archived from the original on 2008-02-19. Retrieved 2008-05-01.
   Marklund, L.; M. Johansson Moller; K. Sandberg; L. Andersson (1996). "A missense mutation in the gene for melanocyte-stimulating hormone receptor (MC1R) is associated with the chestnut coat color in horses". Mammalian Genome. 7 (12): 895–899. doi:10.1007/s003359900264. PMID 8995760. S2CID 29095360.
   "Introduction to Coat Color Genetics". Veterinary Genetics Laboratory. University of California. Archived from the original on 2017-10-10. Retrieved 2008-05-01.
   Haase B; Brooks SA; Schlumbaum A; et al. (2007). "Allelic Heterogeneity at the Equine KIT Locus in Dominant White (W) Horses". PLOS Genetics. 3 (11): e195. doi:10.1371/journal.pgen.0030195. PMC 2065884. PMID 17997609.
   Mau, C.; Poncet, P. A.; Bucher, B.; Stranzinger, G.; Rieder, S. (2004). "Genetic mapping of dominant white (W), a homozygous lethal condition in the horse (Equus caballus)". Journal of Animal Breeding and Genetics. 121 (6): 374–383. doi:10.1111/j.1439-0388.2004.00481.x.
   Ensminger, p. 156
   "How Long is a Horse Pregnant?". Talk of the Turf. Retrieved 2023-03-25.
   Johnson, Tom. "Rare Twin Foals Born at Vet Hospital: Twin Birth Occurrences Number One in Ten Thousand". Communications Services, Oklahoma State University. Oklahoma State University. Archived from the original on 2012-10-12. Retrieved 2008-09-23.
   Miller, Robert M.; Rick Lamb (2005). Revolution in Horsemanship and What it Means to Mankind. Guilford, CT: Lyons Press. pp. 102–103. ISBN 1-59228-387-X. OCLC 57005594.
   Ensminger, p. 150
   Kline, Kevin H. (2010-10-07). "Reducing weaning stress in foals". Montana State University eXtension. Archived from the original on 2012-03-22. Retrieved 2012-04-03.
   Ensminger, M. E. (1991). Horses and Tack (Revised ed.). Boston: Houghton Mifflin Company. p. 129. ISBN 0-395-54413-0. OCLC 21561287.
   McIlwraith, C.W. "Developmental Orthopaedic Disease: Problems of Limbs in young Horses". Orthopaedic Research Center. Colorado State University. Archived from the original on 2013-01-14. Retrieved 2008-04-20.
   Thomas, Heather Smith (2003). Storey's Guide to Training Horses: Ground Work, Driving, Riding. North Adams, MA: Storey Publishing. p. 163. ISBN 1-58017-467-1.
   "2-Year-Old Racing (US and Canada)". Online Fact Book. Jockey Club. Archived from the original on 2013-02-16. Retrieved 2008-04-28.
   Bryant, Jennifer Olson; George Williams (2006). The USDF Guide to Dressage. Storey Publishing. pp. 271–272. ISBN 978-1-58017-529-6. Archived from the original on 2023-03-20. Retrieved 2020-09-28.
   Evans, J. (1990). The Horse (Second ed.). New York: Freeman. p. 90. ISBN 0-7167-1811-1. OCLC 20132967.
   Ensminger, pp. 21–25
   Ensminger, p. 367
   Giffin, p. 304
   Giffin, p. 457
   Fuess, Theresa A. "Yes, The Shin Bone Is Connected to the Ankle Bone". Pet Column. University of Illinois. Archived from the original on September 9, 2006. Retrieved 2008-04-05.
   Giffin, pp. 310–312
   Kreling, Kai (2005). "The Horse's Teeth". Horses' Teeth and Their Problems: Prevention, Recognition, and Treatment. Guilford, CT: Globe Pequot. pp. 12–13. ISBN 1-59228-696-8. OCLC 59163221.[permanent dead link]
   Giffin, p. 175
   Valentine, Beth A.; Van Saun, Robert J.; Thompson, Kent N.; Hintz, Harold F. (2001). "Role of dietary carbohydrate and fat in horses with equine polysaccharide storage myopathy". Journal of the American Veterinary Medical Association. 219 (11): 1537–1544. doi:10.2460/javma.2001.219.1537. PMID 11759989. Archived from the original on 2021-05-11. Retrieved 2021-05-11.
   Ellis, Harold (2010). "The gall bladder and bile ducts". Surgery (Oxford). 28 (5): 218–221. doi:10.1016/j.mpsur.2010.02.007. Archived from the original on 2021-05-12. Retrieved 2021-05-11.
   Ensminger, pp. 309–310
   Sellnow, Les (2004). Happy Trails: Your Complete Guide to Fun and Safe Trail Riding. Eclipse Press. p. 46. ISBN 1-58150-114-5. OCLC 56493380.
   "Eye Position and Animal Agility Study Published". The Horse. March 7, 2010. Archived from the original on 2015-07-23. Retrieved 2010-03-11. Press Release, citing February 2010 Journal of Anatomy, Dr. Nathan Jeffery, co-author, University of Liverpool.
   McDonnell, Sue (June 1, 2007). "In Living Color". The Horse. Archived from the original on 2007-09-27. Retrieved 2007-07-27.
   Briggs, Karen (2013-12-11). "Equine Sense of Smell". The Horse. Archived from the original on 2018-02-01. Retrieved 2013-12-15.
   Myers, Jane (2005). Horse Safe: A Complete Guide to Equine Safety. Collingwood, UK: CSIRO Publishing. p. 7. ISBN 0-643-09245-5. OCLC 65466652. Archived from the original on 2023-03-20. Retrieved 2020-09-28.
   Lesté-Lasserre, Christa (January 18, 2013). "Music Genre's Effect on Horse Behavior Evaluated". The Horse. Blood Horse Publications. Archived from the original on 10 October 2017. Retrieved 23 January 2013.
   Kentucky Equine Research Staff (February 15, 2010). "Radios Causing Gastric Ulcers". EquiNews. Kentucky Equine Research. Archived from the original on 10 October 2017. Retrieved 23 January 2013.
   Thomas, Heather Smith. "True Horse Sense". Thoroughbred Times. Thoroughbred Times Company. Archived from the original on 2012-11-02. Retrieved 2008-07-08.
   Cirelli, Al Jr.; Brenda Cloud. "Horse Handling and Riding Guidelines Part 1: Equine Senses" (PDF). Cooperative Extension. University of Nevada. p. 4. Archived (PDF) from the original on 2015-09-08. Retrieved 2008-07-09.
   Hairston, Rachel; Madelyn Larsen (2004). The Essentials of Horsekeeping. New York: Sterling Publishing Company, Inc. p. 77. ISBN 0-8069-8817-7. OCLC 53186526.
   Miller, p. 28
   Gustavson, Carrie. "Horse Pasture is No Place for Poisonous Plants". Pet Column July 24, 2000. University of Illinois. Archived from the original on August 9, 2007. Retrieved 2008-07-09.
   Harris, p. 32
   Harris, pp. 47–49
   "Fastest speed for a race horse". Guinness World Records. 14 May 2008. Archived from the original on 28 August 2017. Retrieved 8 January 2013.
   Harris, p. 50
   Lieberman, Bobbie (2007). "Easy Gaited Horses". Equus (359): 47–51.
   Equus Staff (2007). "Breeds that Gait". Equus (359): 52–54.
   Harris, pp. 50–55
   "Horse Fight vs Flight Instinct". eXtension. 2009-09-24. Archived from the original on 2013-05-15. Retrieved 2013-04-17.
   McBane, Susan (1992). A Natural Approach to Horse Management. London: Methuen. pp. 226–228. ISBN 0-413-62370-X. OCLC 26359746.
   Ensminger, pp. 305–309
   Prince, Eleanor F.; Gaydell M. Collier (1974). Basic Horsemanship: English and Western. New York: Doubleday. pp. 214–223. ISBN 0-385-06587-6. OCLC 873660.
   Clarkson, Neil (2007-04-16). "Understanding horse intelligence". Horsetalk 2007. Horsetalk. Archived from the original on 2013-01-24. Retrieved 2008-09-16.
   Dorrance, Bill (1999). True horsemanship through feel. Guilford, CT: The Lion Press. p. 1. ISBN 1-58574-321-6.
   Lesté-Lasserre, Christa. "Horses Demonstrate Ability to Count in New Study". The Horse. Archived from the original on 2016-01-01. Retrieved 2009-12-06.
   Coarse, Jim (2008-06-17). "What Big Brown Couldn't Tell You and Mr. Ed Kept to Himself (part 1)". The Blood Horse. Archived from the original on 2012-05-21. Retrieved 2008-09-16.
   Belknap, p. 255
   Belknap, p. 112
   Ensminger, pp. 71–73
   Ensminger, p. 84
   Price, p. 18
   DeFilippis, Chris (2006). The Everything Horse Care Book. Avon, MA: Adams Media. p. 4. ISBN 978-1-59337-530-0. OCLC 223814651.
   Whitaker, p. 43
   Whitaker, pp. 194–197
   Price, p. 15
   Bongianni, entry 87
   Ensminger, pp. 124–125
   Bennett, Deb (1998). Conquerors: The Roots of New World Horsemanship (First ed.). Solvang, CA: Amigo Publications, Inc. p. 7. ISBN 0-9658533-0-6. OCLC 39709067.
   Edwards, pp. 122–123
   Examples are the Australian Riding Pony and the Connemara, see Edwards, pp. 178–179, 208–209
   Price, Steven D.; Shiers, Jessie (2007). The Lyons Press Horseman's Dictionary (Revised ed.). Guilford, CT: Lyons Press. p. 231. ISBN 978-1-59921-036-0.
   Belknap, p. 523
   Pascoe, Elaine. "How Horses Sleep". Equisearch.com. Archived from the original on 2007-09-27. Retrieved 2007-03-23.
   Pascoe, Elaine (2002-03-12). "How Horses Sleep, Pt. 2 – Power Naps". Equisearch.com. Archived from the original on 2007-09-27. Retrieved 2007-03-23.
   Ensminger, p. 310.
   Holland, Jennifer S. (July 2011). "40 Winks?". National Geographic. 220 (1).
   EQUUS Magazine Staff. "Equine Sleep Disorder Videos". Equisearch.com. Archived from the original on 2007-05-10. Retrieved 2007-03-23.
   Smith, BP (1996). Large Animal Internal Medicine (Second ed.). St. Louis, MO: Mosby. pp. 1086–1087. ISBN 0-8151-7724-0. OCLC 33439780.
   Budiansky, Stephen (1997). The Nature of Horses. New York: Free Press. p. 31. ISBN 0-684-82768-9. OCLC 35723713.
   Myers, Phil. "Order Perissodactyla". Animal Diversity Web. University of Michigan. Archived from the original on 2013-01-22. Retrieved 2008-07-09.
   "Hyracotherium". Fossil Horses in Cyberspace. Florida Museum of Natural History. Archived from the original on 2013-01-31. Retrieved 2008-07-09.
   "Mesohippus". Fossil Horses in Cyberspace. Florida Museum of Natural History. Archived from the original on 2013-01-22. Retrieved 2008-07-09.
   "The Evolution of Horses". The Horse. American Museum of Natural History. Archived from the original on 2013-01-28. Retrieved 2008-07-09.
   Miller, p. 20
   "Equus". Fossil Horses in Cyberspace. Florida Museum of Natural History. Archived from the original on 2013-01-22. Retrieved 2008-07-09.
   Weinstock, J.; et al. (2005). "Evolution, Systematics, and Phylogeography of Pleistocene Horses in the New World: A Molecular Perspective". PLOS Biology. 3 (8): e241. doi:10.1371/journal.pbio.0030241. PMC 1159165. PMID 15974804.
   Vila, C.; et al. (2001). "Widespread Origins of Domestic Horse Lineages" (PDF). Science. 291 (5503): 474–477. Bibcode:2001Sci...291..474V. doi:10.1126/science.291.5503.474. PMID 11161199. Archived from the original (PDF) on 2012-10-13. Retrieved 2009-03-17.
   Luís, Cristina; et al. (2006). "Iberian Origins of New World Horse Breeds". Quaternary Science Reviews. 97 (2): 107–113. doi:10.1093/jhered/esj020. PMID 16489143.
   Haile, James; et al. (2009). "Ancient DNA reveals late survival of mammoth and horse in interior Alaska". PNAS. 106 (52): 22352–22357. Bibcode:2009PNAS..10622352H. doi:10.1073/pnas.0912510106. PMC 2795395. PMID 20018740.
   Buck, Caitlin E.; Bard, Edouard (2007). "A calendar chronology for Pleistocene mammoth and horse extinction in North America based on Bayesian radiocarbon calibration". Quaternary Science Reviews. 26 (17–18): 2031–2035. Bibcode:2007QSRv...26.2031B. doi:10.1016/j.quascirev.2007.06.013. Archived from the original on 2018-11-06. Retrieved 2017-09-06.
   LeQuire, Elise (2004-01-04). "No Grass, No Horse". The Horse. Archived from the original on 2013-01-09. Retrieved 2009-06-08.
   Olsen, Sandra L. (1996). "Horse Hunters of the Ice Age". Horses Through Time (First ed.). Boulder, CO: Roberts Rinehart Publishers. p. 46. ISBN 1-57098-060-8. OCLC 36179575.
   "An extraordinary return from the brink of extinction for world's last wild horse". ZSL Press Releases. Zoological Society of London. 2005-12-19. Archived from the original on 2013-05-16. Retrieved 2012-06-06.
   "Home". The Foundation for the Preservation and Protection of the Przewalski Horse. Archived from the original on 2017-10-10. Retrieved 2008-04-03.
   Dohner, pp. 298–299
   Pennisi, Elizabeth (22 February 2018). "Ancient DNA upends the horse family tree". sciencemag.org. Archived from the original on 21 September 2022. Retrieved 30 June 2022.
   Orlando, Ludovic; Outram, Alan K.; Librado, Pablo; Willerslev, Eske; Zaibert, Viktor; Merz, Ilja; Merz, Victor; Wallner, Barbara; Ludwig, Arne (6 April 2018). "Ancient genomes revisit the ancestry of domestic and Przewalski's horses". Science. 360 (6384): 111–114. Bibcode:2018Sci...360..111G. doi:10.1126/science.aao3297. hdl:10871/31710. ISSN 0036-8075. PMID 29472442.
   "Ancient DNA rules out archeologists' best bet for horse domestication". ArsTechnica. February 25, 2018. Archived from the original on 25 June 2020. Retrieved 24 June 2020.
   Dohner, p. 300
   "Tarpan". Breeds of Livestock. Oklahoma State University. Archived from the original on 2009-01-16. Retrieved 2009-01-13.
   "Ponies from the past?: Oregon couple revives prehistoric Tarpan horses". The Daily Courier. June 21, 2002. Archived from the original on 2021-04-17. Retrieved 2009-10-21.
   Peissel, Michel (2002). Tibet: The Secret Continent. Macmillan. p. 36. ISBN 0-312-30953-8. Archived from the original on 2023-03-20. Retrieved 2020-09-28.
   Royo, L.J.; Álvarez, I.; Beja-Pereira, A.; Molina, A.; Fernández, I.; Jordana, J.; Gómez, E.; Gutiérrez, J. P.; Goyache, F. (2005). "The Origins of Iberian Horses Assessed via Mitochondrial DNA". Journal of Heredity. 96 (6): 663–669. doi:10.1093/jhered/esi116. PMID 16251517.
   Edwards, pp. 104–105
   Lira, Jaime; et al. (2010). "Ancient DNA reveals traces of Iberian Neolithic and Bronze Age lineages in modern Iberian horses" (PDF). Molecular Ecology. 19 (1): 64–78. doi:10.1111/j.1365-294X.2009.04430.x. PMID 19943892. S2CID 1376591. Archived (PDF) from the original on 2017-08-10. Retrieved 2018-04-20.
   Pallas (1775). "Equus hemionus". Wilson & Reeder's mammal species of the world. Bucknell University. Archived from the original on September 26, 2013. Retrieved September 1, 2010.
   "Mule Information". BMS Website. British Mule Society. Archived from the original on 2017-10-10. Retrieved 2008-07-10.
   "Zebra hybrid is cute surprise". BBC News. June 26, 2001. Archived from the original on 2017-06-14. Retrieved 2010-02-06.
   "Befuddling Birth: The Case of the Mule's Foal". NPR.org. National Public Radio. Archived from the original on 2008-12-06. Retrieved 2008-08-16.
   Outram, A. K.; Stear, N. A.; Bendrey, R; Olsen, S; Kasparov, A; Zaibert, V; Thorpe, N; Evershed, R. P. (2009). "The earliest horse harnessing and milking". Science. 323 (5919): 1332–1335. Bibcode:2009Sci...323.1332O. doi:10.1126/science.1168594. PMID 19265018. S2CID 5126719.
   Matossian, Mary Kilbourne (1997). Shaping World History: Breakthroughs in Ecology, Technology, Science, and Politics. Armonk, NY: M.E. Sharpe. p. 43. ISBN 0-585-02397-2. OCLC 156944228. Archived from the original on 2023-03-20. Retrieved 2020-09-28.
   "Horsey-aeology, Binary Black Holes, Tracking Red Tides, Fish Re-evolution, Walk Like a Man, Fact or Fiction". Quirks and Quarks Podcast with Bob Macdonald. CBC Radio. 2009-03-07. Archived from the original on 2014-10-07. Retrieved 2010-09-18.
   Evans, James Warren (1992). Horse Breeding and Management. Amsterdam: Elsevier Health Sciences. p. 56. ISBN 0-444-88282-0. OCLC 243738023.[permanent dead link]
   Kuznetsov, P. F. (2006). "The emergence of Bronze Age chariots in eastern Europe". Antiquity. 80 (309): 638–645. doi:10.1017/S0003598X00094096. S2CID 162580424.
   Lambert, Jonathan (20 October 2021). "Scientists found modern domestic horses' homeland in southwestern Russia". Science News. Archived from the original on 14 November 2021. Retrieved 14 November 2021.
   Pablo Librado; et al. (October 2021). "The origins and spread of domestic horses from the Western Eurasian steppes". Nature. 598 (7882): 634–640. Bibcode:2021Natur.598..634L. doi:10.1038/s41586-021-04018-9. ISSN 1476-4687. PMC 8550961. PMID 34671162.
   Lau, A. N.; Peng, L.; Goto, H.; Chemnick, L.; Ryder, O. A.; Makova, K. D. (2009). "Horse Domestication and Conservation Genetics of Przewalski's Horse Inferred from Sex Chromosomal and Autosomal Sequences". Molecular Biology and Evolution. 26 (1): 199–208. doi:10.1093/molbev/msn239. PMID 18931383.
   Lindgren, Gabriella; Niclas Backström; June Swinburne; Linda Hellborg; Annika Einarsson; Kaj Sandberg; Gus Cothran; Carles Vilà; Matthew Binns; Hans Ellegren (2004). "Limited number of patrilines in horse domestication". Nature Genetics. 36 (4): 335–336. doi:10.1038/ng1326. PMID 15034578.
   Vilà, C.; et al. (2001). "Widespread origins of domestic horse lineages". Science. 291 (5503): 474–477. Bibcode:2001Sci...291..474V. doi:10.1126/science.291.5503.474. PMID 11161199.
   Cai, D. W.; Tang, Z. W.; Han, L.; Speller, C. F.; Yang, D. Y. Y.; Ma, X. L.; Cao, J. E.; Zhu, H.; Zhou, H.; et al. (2009). "Ancient DNA provides new insights into the origin of the Chinese domestic horse" (PDF). Journal of Archaeological Science. 36 (3): 835–842. Bibcode:2009JArSc..36..835C. doi:10.1016/j.jas.2008.11.006. Archived (PDF) from the original on 29 June 2011. Retrieved 17 January 2011.
   Olsen, Sandra L. (2006). "Early Horse Domestication: Weighing the Evidence". In Olsen, Sandra L; Grant, Susan; Choyke, Alice M.; Bartosiewicz, Laszlo (eds.). Horses & Humans: The Evolution of Human-Equine Relationships. Oxford, UK: Archaeopress. pp. 81–113. ISBN 978-1-84171-990-0.
   Epstein, H. (1955). "Domestication Features in Animals as Functions of Human Society". Agricultural History Society. 29 (4): 137–146. JSTOR 3740046.
   Ludwig, A.; Pruvost, M.; Reissmann, M.; Benecke, N.; Brockmann, G.A.; Castanos, P.; Cieslak, M.; Lippold, S.; Llorente, L.; et al. (2009). "Coat Color Variation at the Beginning of Horse Domestication". Science. 324 (5926): 485. Bibcode:2009Sci...324..485L. doi:10.1126/science.1172750. PMC 5102060. PMID 19390039.
   Edwards, Gladys Brown (1973). The Arabian: War Horse to Show Horse (Revised Collectors ed.). Rich Publishing. pp. 1, 3.
   Edwards, p. 291
   Anthony, David W. (1996). "Bridling Horse Power: The Domestication of the Horse". Horses Through Time (First ed.). Boulder, CO: Roberts Rinehart Publishers. pp. 66–67. ISBN 1-57098-060-8. OCLC 36179575.
   Olsen, Sandra L. "Horses in Prehistory". Anthropology Research. Carnegie Museum of Natural History. Archived from the original on May 25, 2008. Retrieved 2008-08-16.
   Lesté-Lasserre, Christa (October 7, 2009). "Mares' Social Bonds Might Enhance Reproductive Success". The Horse. Archived from the original on April 15, 2012. Retrieved 2009-10-21.
   "Animals on the Moor". Dartmoor Commoners' Council. Archived from the original on 2017-10-10. Retrieved 2012-03-29.
   Fear, Sally (2006). New Forest Drift: A Photographic Portrait of Life in the National Park. Perspective Photo Press. p. 75. ISBN 978-0-9553253-0-4.
   Ensminger, p. 424
   Edwards, Gladys Brown (1973). The Arabian: War Horse to Show Horse (Revised Collectors ed.). Rich Publishing. pp. 22–23.
   "Is Purity the Issue?". WAHO Publication Number 21 January 1998. World Arabian Horse Organization. Archived from the original on 5 July 2008. Retrieved 2008-04-29.
   "Andalusian". Breeds of Livestock. Oklahoma State University. Archived from the original on 2008-03-12. Retrieved 2008-04-29.
   Sponenberg, p. 155
   Sponenberg, pp. 156–157
   Sponenberg, p. 162
   "History of Thoroughbreds". Britishhorseracing.com. British Horseracing Authority. Archived from the original on 2014-02-01. Retrieved 2008-04-03.
   Hedge, Juliet; Don M. Wagoner (2004). Horse Conformation: Structure, Soundness and Performance. Guilford, CT: Globe Pequot. pp. 307–308. ISBN 1-59228-487-6. OCLC 56012597.
   "FAO Stat – Live Animals". Food and Agriculture Organization. December 16, 2009. Archived from the original on 2013-01-19. Retrieved 2010-02-05.
   "Most Comprehensive Horse Study Ever Reveals A Nearly $40 Billion Impact On The U.S. Economy" (PDF) (Press release). American Horse Council. Archived from the original (PDF) on June 25, 2006. Retrieved 2005-06-20.
   "Tiger tops dog as world's favourite animal". Independent Online. Independent. Archived from the original on 2012-10-28. Retrieved 2011-06-01.
   Olsen, Sandra L. (1996). "In the Winner's Circle: The History of Equestrian Sports". Horses Through Time (First ed.). Boulder, CO: Roberts Rinehart Publishers. pp. 105, 111–113, 121. ISBN 1-57098-060-8. OCLC 36179575.
   Edwards, Elwyn Hartley (2002). Horses (Second American ed.). New York: Dorling Kindersley. pp. 32–34. ISBN 0-7894-8982-1. OCLC 50798049.
   Self, Margaret Cabell (2005). Riding Simplified. Kessinger Publishing. p. 55. ISBN 1-4191-0087-4.[permanent dead link]
   Thorson, Juli S. (2006). "Rugged Lark". In Martindale, Cathy and Kathy Swan (ed.). Legends 7: Outstanding Quarter Horse Stallions and Mares. Colorado Springs, CO: Western Horseman. p. 218. ISBN 978-0-911647-79-2.
   Mettler, John J Jr. (1989). Horse Sense: A Complete Guide to Horse Selection and Care. Pownal, VT: Storey Communications, Inc. pp. 47–54. ISBN 0-88266-549-9. OCLC 19324181.
   Edwards, pp. 346–356, 366–371
   Edwards, pp. 376–377
   Edwards, p. 360
   Collins, Tony; Martin, John; Vamplew, Wray (2005). Encyclopedia of Traditional British Rural Sports. London: Routledge. pp. 173–174. ISBN 0-415-35224-X. OCLC 57005595. Archived from the original on 2023-03-20. Retrieved 2020-09-28.
   Edwards, pp. 332–337
   Campbell, B.N. (2001). National Gambling Impact Study Commission Final Report (1999). Darby, PA: DIANE Publishing. p. 111. ISBN 0-7567-0701-3. Archived from the original on 2023-03-20. Retrieved 2015-11-15.
   "Horse Mounted Unit". United States Park Police. National Park Service. Archived from the original on February 18, 2008. Retrieved 2008-04-07.
   Edwards, pp. 226–227
   "Volunteer Mounted Search and Rescue Unit". Employment. San Benito County Sheriff's Office. Archived from the original on 2008-05-09. Retrieved 2008-07-08.
   US Forest Service (May 2003). "Mules Key in Accomplishing Trail Work" (PDF). Success Stories. US Department of Agriculture. p. 4. Archived (PDF) from the original on 2008-05-27. Retrieved 2008-04-20.
   Brown, Kimberly S. (June 1, 2006). "At Work in Morocco". The Horse. Archived from the original on 2007-12-22. Retrieved 2009-10-21.
   Gifford, Angela (2000) [1998]. "Working Draught Horses as Singles and Pairs". The Working Horse Manual. Tonbridge, UK: Farming Press. p. 85. ISBN 0-85236-401-6. OCLC 40464050.
   Miller, Lynn R. (2000) [1981]. Work Horse Handbook (First Edition, Fifteenth Impression ed.). Sisters, OR: Small Farmer's Journal Inc. p. 13. ISBN 0-9607268-0-2. OCLC 234277549.
   Gifford, Angela (2000) [1998]. "Working Horses in Forestry". The Working Horse Manual. Tonbridge, UK: Farming Press. p. 145. ISBN 0-85236-401-6. OCLC 40464050.
   Newby, Jonica; Diamond, Jared; Anthony, David (1999-11-13). "The Horse in History". The Science Show. Radio National. Archived from the original on 2013-01-19. Retrieved 2012-01-04.
   Anthony, David W.; Dorcas R. Brown. "The Earliest Horseback Riding and its Relation to Chariotry and Warfare". Harnessing Horsepower. Institute for Ancient Equestrian Studies. Archived from the original on 2017-10-10. Retrieved 2007-10-09.
   Whitaker, pp. 30–31
   Lacey, Marc (2004-05-04). "In Sudan, Militiamen on Horses Uproot a Million". The New York Times. Archived from the original on 2009-04-23. Retrieved 2011-01-04.
   Stoddard, Samuel. "Unit Activities". Co H, 4th Virginia Cavalry. Washington Webworks, LLC. Archived from the original on 2008-01-18. Retrieved 2008-04-29.
   "Transport". British Monarchy. Archived from the original on 2009-02-16. Retrieved 2009-08-30.
   McWilliams, Jeremiah (December 3, 2008). "Anheuser-Busch gives face time to Budweiser Clydesdales". St. Louis Post-Dispatch. Archived from the original on 2012-05-14. Retrieved 2010-09-18.
   Sellnow, Les (March 1, 2006). "Hollywood Horses". The Horse. Archived from the original on 2011-09-05. Retrieved 2009-10-21.
   "Trademark Horse – Horses as advertising mediums". Westfälische Pferdemuseum (Westphalian Horse Museum). Archived from the original on 2008-10-11. Retrieved 2008-08-16.
   Fox-Davies, Arthur Charles (2007). A Complete Guide to Heraldry. Skyhorse Publishing Inc. p. 201. ISBN 978-1-60239-001-0. Archived from the original on 2023-03-20. Retrieved 2020-09-28.
   Tozer, Basil (1908). The Horse in History. London: Methuen. pp. 94, 98–100. OCLC 2484673.
   "Year of the Horse". Chinese Culture Center of San Francisco. Archived from the original on 2011-07-16. Retrieved 2007-07-22.
   Cole, Craig (8 November 2021). "Giddy Up: Top 10 Horse-Themed Cars". Autoguide.com. Archived from the original on 25 May 2022. Retrieved 7 July 2022.
   "Cars with Horse Logos: How Many of Them do You Know?". 9 January 2022. Archived from the original on 28 May 2022. Retrieved 18 June 2022.
   "Top 11 cars named after horses, which is your favorite?". 8 May 2021. Archived from the original on 16 August 2022. Retrieved 18 June 2022.
   Bush, Karen; Julian Marczak (2005). The Principles of Teaching Riding: The Official Manual of the Association of British Riding Schools. David & Charles. p. 58. ISBN 0-7153-1902-7. OCLC 224946044.[permanent dead link]
   "About Para Equestrian Dressage". Federation Equestre Internationale. Archived from the original on 2013-05-08. Retrieved 2010-03-07.
   "Frequently Asked Questions About Hippotherapy" (PDF). FAQ – AHA, April 2005. American Hippotherapy Association. Archived from the original (PDF) on September 19, 2007. Retrieved 2008-07-08.
   "Equine Facilitated Psychotherapy (EFP) Fact Sheet". Equine Facilitated Mental Health Association. Archived from the original on April 30, 2008. Retrieved 2008-07-08.
   Wise, Mike (2003-08-10). "Partners, Horse and Man, in Prison Pasture". New York Times. Retrieved 2008-07-08.
   Frazier, Ian (2005-04-18). "Invaders: Destroying Baghdad". The New Yorker. Archived from the original on 2017-10-10. Retrieved 2008-04-03.
   Ballard, Pepper (August 19, 2001). "A Good Life for Horses at the Duchess Sanctuary". The Humane Society of the United States. Archived from the original on 2013-01-28. Retrieved 2011-06-01.
   McCutcheon, Marc (2000). Descriptionary: A Thematic Dictionary (Second ed.). New York: Checkmark Books (Facts On File imprint). p. 285. ISBN 0-8160-4105-9.
   "FAOSTAT". Food and Agriculture Organization of the United Nations. Archived from the original on 2019-05-24. Retrieved 2019-10-25.
   "U.S.D.A. Promotes Horse & Goat Meat". I.G.H.A./HorseAid's U.S.D.A. Report. U.S. Department of Agriculture. Archived from the original on 2017-10-10. Retrieved 2008-04-03.
   Coile, Zachary (2006-09-08). "House votes to outlaw slaughter of horses for human consumption". SF Gate. San Francisco Chronicle. Archived from the original on 2012-11-23. Retrieved 2008-04-03.
   Ockerman, Herbert W.; Hansen, Conly L. (2000). Animal By-product Processing & Utilization. Lancaster, PA: CRC Press. p. 129. ISBN 1-56676-777-6. OCLC 43685745.
   "Inside a Modern Baseball". Baseball Fever. Baseball Almanac. Archived from the original on 2013-08-12. Retrieved 2008-04-03.
   Bartlett, Virginia K. (1994). Keeping House: Women's Lives in Western Pennsylvania, 1790–1850. University of Pittsburgh Press. pp. 34–35. ISBN 0-8229-5538-5. OCLC 30978921. Archived from the original on 2023-03-20. Retrieved 2020-09-28.
   MacGregor, Arthur (1985). Bone, Antler, Ivory and Horn: Technology of Skeletal Materials Since the Roman Period. Totowa, NJ: Barnes & Noble. p. 31. ISBN 0-389-20531-1. OCLC 11090630.
   Fort, Matthew (2005). Eating Up Italy: Voyages on a Vespa. London: Centro Books. p. 171. ISBN 0-00-721481-2. OCLC 60419304.
   Diseases of the Stomach and Intestines. Translated by Hurd, Edward Payson. New York: W. Wood & Company. 1886. p. 29.
   Kellon, Eleanor (2008). "Focus on Feed Costs". Horse Journal. 16 (6): 11–12.
   Hall, Marvin H.; Patricia M. Comerford (1992). "Pasture and Hay for Horses – Agronomy Facts 32" (PDF). Cooperative Extension Service. University of Pennsylvania. Archived from the original (PDF) on 2012-12-24. Retrieved 2007-02-14.
   Giffin, pp. 476–477
   "Feeding Factors". Horse Nutrition. Ohio State University. Archived from the original on 2009-07-08. Retrieved 2007-02-09.
   Giffin, p. 455
   Giffin, p. 482
   Giffin, pp. 62, 168, 310
   Harris, Susan E. (1994). The United States Pony Club Manual of Horsemanship: Basics for Beginners – D Level. New York: Howell Book House. pp. 160–161. ISBN 0-87605-952-3.
   Wheeler, Eileen (2006). "Fence Planning". Horse Stable And Riding Arena Design. Armes, IA: Blackwell Publishing. p. 215. ISBN 978-0-8138-2859-6. OCLC 224324847. Archived from the original on 2023-03-20. Retrieved 2020-09-28.
   Giffin, p. 90
   Kang, Hyungsuk; Zsoldos, Rebeka R.; Sole-Guitart, Albert; Narayan, Edward; Cawdell-Smith, A. Judith; Gaughan, John B. (15 April 2023). "Heat stress in horses: a literature review". International Journal of Biometeorology. 67 (6): 957–973. Bibcode:2023IJBm...67..957K. doi:10.1007/s00484-023-02467-7. PMC 10267279. PMID 37060454.
   McCutcheon, L. Jill; Geor, Raymond J. (1998). "Sweating: Fluid and Ion Losses and Replacement". Veterinary Clinics of North America: Equine Practice. 14 (1): 75–95. doi:10.1016/s0749-0739(17)30213-4. ISSN 0749-0739.
   McDonald, Rhona E.; Fleming, Rachel I.; Beeley, John G.; Bovell, Douglas L.; Lu, Jian R.; Zhao, Xiubo; Cooper, Alan; Kennedy, Malcolm W. (2009). "Latherin: A Surfactant Protein of Horse Sweat and Saliva". PLoS One. 4 (5): e5726. doi:10.1371/journal.pone.0005726. ISSN 1932-6203. PMC 2684629.
   Gao, Hongyan; Wang, Long; Ma, Jun; Gao, Xiang; Xiao, Jianhua; Wang, Hongbing (29 October 2021). "Modeling the current distribution suitability and future dynamics of Culicoides imicola under climate change scenarios". PeerJ Life & Environment. 9: e12308. doi:10.7717/peerj.12308. PMC 8559603. PMID 34760364.
   Martin, Gerardo; Yanez-Arenas, Carlos; Chen, Carla; Plowright, Raina K.; Webb, Rebecca J.; Skerratt, Lee F. (19 March 2018). "Climate Change Could Increase the Geographic Extent of Hendra Virus Spillover Risk". EcoHealth. 15 (3): 509–525. doi:10.1007/s10393-018-1322-9. PMC 6245089. PMID 29556762.
  Sources
  Belknap, Maria (2004). Horsewords: The Equine Dictionary (Second ed.). North Pomfret, VT: Trafalgar Square Publishing. ISBN 1-57076-274-0.
  Bongianni, Maurizio (1987). Simon & Schuster's Guide to Horses and Ponies. New York: Fireside. ISBN 0-671-66068-3.
  Dohner, Janet Vorwald (2001). "Equines: Natural History". In Dohner, Janet Vorwald (ed.). Historic and Endangered Livestock and Poultry Breeds. Topeka, KS: Yale University Press. pp. 400–401. ISBN 0-300-08880-9.
  Edwards, Elwyn Hartley (1994). The Encyclopedia of the Horse. London: Dorling Kindersley. ISBN 1-56458-614-6. OCLC 29670649.
  Ensminger, M. E. (1990). Horses and Horsemanship: Animal Agricultural Series (Sixth ed.). Danville, IN: Interstate Publishers. ISBN 0-8134-2883-1. OCLC 21977751.
  Giffin, James M.; Tom Gore (1998). Horse Owner's Veterinary Handbook (Second ed.). New York: Howell Book House. ISBN 0-87605-606-0. OCLC 37245445.
  Harris, Susan E. (1993). Horse Gaits, Balance and Movement. New York: Howell Book House. ISBN 0-87605-955-8. OCLC 25873158.
  McBane, Susan (1997). The Illustrated Encyclopedia of Horse Breeds. Edison, NJ: Wellfleet Press. ISBN 0-7858-0604-0. OCLC 244110821.
  Miller, Robert M. (1999). Understanding the Ancient Secrets of the Horse's Mind. Neenah, WI: Russell Meerdink Company Ltd. ISBN 0-929346-65-3. OCLC 42389612. Archived from the original on 2023-03-20. Retrieved 2020-09-28.
  Price, Steven D.; Spector, David L.; Rentsch, Gail; Burn, Barbara B., eds. (1998). The Whole Horse Catalog: Revised and Updated (Revised ed.). New York: Fireside. ISBN 0-684-83995-4.
  Sponenberg, D. Phillip (1996). "The Proliferation of Horse Breeds". Horses Through Time (First ed.). Boulder, CO: Roberts Rinehart Publishers. ISBN 1-57098-060-8. OCLC 36179575.
  Whitaker, Julie; Whitelaw, Ian (2007). The Horse: A Miscellany of Equine Knowledge. New York: St. Martin's Press. ISBN 978-0-312-37108-1.
  Further reading
  Chamberlin, J. Edward (2006). Horse: How the Horse Has Shaped Civilizations. New York: Bluebridge. ISBN 978-0-9742405-9-6. OCLC 61704732.
  External links

  Wikispecies has information related to Equus caballus.
  "Ancient horse bone yields oldest DNA sequence"
  "Horse" . New International Encyclopedia. 1905.
  "Horse" . Encyclopædia Britannica (11th ed.). 1911.
  Genome of Equus caballus, via Ensembl
  Genome of Equus caballus (version EquCab3.0/equCab3), via UCSC Genome Browser
  Data of the genome of Equus caballus, via NCBI
  Data of the genome assembly of Equus caballus (versión EquCab3.0/equCab3), via NCBI
  vte
  Extant Perissodactyla (Odd-toed ungulates) species by suborder
  vte
  Horses
  vte
  Working animals
  Portal:
  icon Horses
  Horse at Wikipedia's sister projects:

  Media from Commons

  Quotations from Wikiquote

  Taxa from Wikispecies
  Taxon identifiers	
  Wikidata: Q726Wikispecies: Equus caballusTSA: 6615
  Authority control databases Edit this at Wikidata
  Categories: Domesticated animalsHorsesAnimal-powered transportMammals described in 1758Taxa named by Carl LinnaeusEquus (genus)Herbivorous mammalsHorse subspeciesLivestockNational symbols of Burkina FasoNational symbols of LesothoNational symbols of MongoliaNational symbols of NigeriaNational symbols of TurkmenistanPack animalsSymbols of New Jersey
  '''


app.run(debug=True, host="0.0.0.0")
