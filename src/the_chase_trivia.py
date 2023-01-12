import random
import time



FLASH_QUESTIONS = {
    "  In what year was the first-ever Wimbledon Championship held? ": "1877",
    "  Hg is the chemical symbol of which element? ": "Mercury",
    "  Which email service is owned by Microsoft? ": "Hotmail",
    "  Which country produces the most coffee in the world? ": "Brazil",
    "  In which city was Jim Morrison buried? ": "Paris",
    "  Which song by Luis Fonsi and Daddy Yankee has the most views (of all time) on YouTube? ": "'Despacito '",
    "  What was the first state? ": "Delaware",
    "  What is the capital city of Spain? ": "Madrid",
    "  What is Chandler's last name in the sitcom Friends? ": "Bing",
    "  About how many taste buds does the average human tongue have? ": "10000",
    "  How much does the Chewbacca costume weigh? (in pounds) ": "8",
    "  Globe and Jerusalem are types of what? ": "Artichoke",
    "  Which is the highest waterfall in the world? ": "Angel Falls",
    "  Ludwig Van Beethoven was born in 1770 in which city? ": "Berlin",
    "  What is the third sign of the zodiac? ": "Gemini",
    "  What is Ariana Grande's brother's name? ": "Frankie",
    "  Who discovered penicillin? (last name) ": "Fleming",
    "  Which name is rapper Sean Combs better known by? ": "P  Diddy",
    "  Which country invented tea? ": "China",
    "  Pure water has a pH level of around? (number) ": "7",
    "  Which is the only vowel on a standard keyboard that is not on the top line of letters? ": "A",
    "  Who starts first in chess? ": "White",
    "  What was Britney Spears' first song? ": "'Baby One More Time '",
    "  What did Queen Anne die of? ": "stroke",
    "  Groups of lions are known as what? ": "Prides",
    "  How many pairs of wings does a bee have? ": "Two",
    "  What language has the most words? ": "English",
    "  What's the most expensive home in the world? ": "Buckingham Palace",
    "  Kodiak island is in which US state? ": "Alaska",
    "  Which castle is on the island of Anglesey? ": "Beaumaris",
    "  Which reality show series is Andy Cohen's favorite? ": "The Real Housewives",
    "  How long does it take to hard boil an egg? (in minutes) ": "7",
    "  What nationality was Marco Polo? ": "Venetian",
    "  Which scientist was awarded the 1921 Nobel Prize in physics? ": "Albert Einstein",
    "  Name the world's largest ocean  ": "Pacific",
    "  What did the Crocodile swallow in Peter Pan? ": "alarm clock",
    "  What state is the Lincoln family home (Hildene) located in? ": "Vermont",
    " Zurich is the largest city in what country? ": "Switzerland",
    "  How many phases of the moon are there? ": "Eight",
    "  What's the hardest rock? ": "diamond",
    "  How many bones do sharks have in their bodies? (number) ": "0",
    "  The fear referred to as arachnophobia indicates a fear of what? ": "Spiders",
    "  What color is a Himalayan poppy flower? ": "Blue",
    "  What was the name of the family who starred in 7th Heaven? ": "The Camdens",
    "  Name the world's biggest island  ": "Greenland",
    " Which sport does Costantino Rocca play? ": "Golf",
    "  Which boxer was known as 'The Greatest' and 'The People's Champion'? ": "Muhammad Ali",
    "  What flavor is Cointreau? ": "Orange",
    "  Which country is Prague in? ": "Czech Republic",
    "  Who was the first American to go into space? ": "Alan Shephard",
    "  How many hearts does an octopus have? (number) ": "3",
    "  What is the name of the thin but long country that spans more than half of the western coast of South America? ": "Chile",
    "  Which planet has the most gravity? ": "Jupiter",
    "  What was Beyonce's first solo album? ": "Dangerously In Love",
    " Which country did AC/DC originate in? ": "Australia",
    "  In what state did the first official American baseball game take place? ": "New Jersey",
    "  Which mammal doesn't have vocal cords? ": "Giraffe",
    "  The colored part of the human eye that controls how much light passes through the pupil is called what? ": "Iris",
    " What year did the Titanic movie come out? ": "1997",
    "  What is the national dish of Spain? ": "Paella",
    " Who sang the song, 'My Way'? ": "Frank Sinatra",
    "  Which horoscope sign has a crab? ": "Cancer",
    "  How many rides are at Disney World? ": "46",
    "  What is sushi traditionally wrapped in? ": "Edible seaweed",
    "  What color is Absynthe? ": "Green",
    " When did the Cold War end? ": "1989",
    " Which company owns Bugatti, Lamborghini, Audi, Porsche, and Ducati? ": "Volkswagen",
    "  The Statue of Liberty was given to the US by which country? ": "France",
    "  Google Chrome, Safari, Firefox, and Explorer are different types of what? ": "Web browsers",
    "  Which US city is known as the City of Brotherly Love? ": "Philadelphia",
    "  What substance are nails made out of? ": "Keratin",
    "  Which instrument did John Lennon play in the Beatles? ": "Rhythm guitar",
    "  How many children does Oprah Winfrey have? (number) ": "0",
    "  How many weeks are in a year? ": "52",
    "  Who played Neo in The Matrix? ": "Keanu Reeves",
    "  In what year was the first episode of South Park aired? ": "1997",
    "  What is the largest bone in the human body? ": "femur",
    "  How many national parks are in the United States? ": "58",
    "  What is the symbol for potassium? ": "K",
    "  What is allspice alternatively known as? ": "Pimento",
    "  Which desert is the largest in the world? ": "Sahara",
    "  How old is Lil' Wayne? (number) ": "37",
    "  What is the only American state that begins with the letter 'p'? ": "Pennsylvania",
    "  What is the world's longest river? ": "Amazon",
    "  What's the first letter on a typewriter? ": "Q",
    "  Which kind of flower bulbs were once exchanged as a form of currency? ": "Tulips",
    "  Name the Spanish artist, sculptor, and draughtsman famous for co-founding the Cubist movement (full name)  ": "Pablo Picasso",
    "  What year was Walt Disney born? ": "1901",
    "  Which Williams sister has won more Grand Slam titles? ": "Serena",
    " Which planet is known as the red planet? ": "Mars",
    "  What heavenly body was demoted from planet status recently? ": "Pluto",
    "  What does space sound like? ": "Space is silent",
    "  What is the largest planet in our solar system? ": "Jupiter",
    "  What is the real name of Jersey Shore's Snooki? ": "Nicole Polizzi",
    "  Who famously played Bill Clinton on Saturday Night Life? ": "Darrell Hammond",
    "  How many times did Ross Geller marry and divorce on Friends? (number) ": "3",
    "  Who in Hollywood is known as 'The Voice of God'? ": "Morgan Freeman",
    "  What is the fastest fish in the ocean? ": "Sailfish",
    "  What's the medical term for bad breath? ": "Halitosis",
    " How many total time zones are there in the world? ": "24",
    " How long is an eon in geology? (in billions) ": "1",
    "  How many soccer players should each team have on the field at the start of each match? ": "11",
    "  What year was the very first model of the iPhone released? ": "2007",
    "  What does 'HTTP' stand for? ": "HyperText Transfer Protocol",
    "  Who was the first woman to win a Nobel Prize (in 1903)? ": "Marie Curie",
    "  What part of the atom has no electric charge? ": "Neutron",
    "  Where were the Declaration of Independence, the Constitution, and the Bill of Rights stored during World War II? ": "Fort Knox",
    "  When Michael Jordan played for the Chicago Bulls, how many NBA Championships did he win? (number)": "6",
    " Which African country was formerly known as Abyssinia? ": "Ethiopia",
    "  Which singer's real name is Stefani Joanne Angelina Germanotta? ": "Lady Gaga",
    "  Which Jamaican runner is an 11-time world champion and holds the record in the 100 and 200-meter race? ": "Usain Bolt",
    "  How many neck bones does a giraffe have? ": "Seven",
    "  In the movie The Golden Child, what does the child animate to amuse his captor? ": "A Coke can",
    "  Who received the first artificial heart transplant surgery in 1982? ": "Barney Clark",
    "  In which video game did Super Mario first appear? ": "Donkey Kong",
    "  Which animal has the largest eye in the world? ": "The giant squid",
    "  Where would you find the Sea of Tranquility? ": "The moon",
    "  What is someone who shoes horses called? ": "Farrier",
    "  What kind of weapon is a falchion? ": "A sword",
    "  Who invented the rabies vaccine? ": "Louis Pasteur",
    "  Which kind of bulbs were once exchanged as a form of currency? ": "Tulips",
    "  Which chess piece can only move diagonally? ": "Bishop",
    "  How many valves does a trumpet have? (number) ": "3",
    "  Who wrote the Vampire Chronicles, which include the noels Armand, Blood and Gold, and Interview with the Vampire? ": "Anne Rice",
    "  In publishing, what does POD mean? ": "Print on demand",
    "  Who was Henry VIII's first wife? ": "Catherine of Aragon",
    "  What dinosaur fossil was originally mistaken for a type of bison? ": "Triceratops",
    "  What dinosaur name means 'fast thief'? ": "Velociraptor",
    "  How many pairs of legs do millipedes have per body segment? ": "Two pairs",
    "  What's a 'king' honeybee called? ": "drone",
    "  What animal was framed in the unfinished paint-by-number in Rizzo's room in Grease? ": "A horse",
    "  What is the name of the boat in Jaws? ": "Orca",
    "  In what U S  city was the Brown Marmorated Stink Bug first detected? ": "Allentowna",
    " Which insect has been named America's Top Nuisance Pest? ": "Ants",
    "  Which organ do insects not have? ": "Lungs",
    "  What is the strongest insect for its size? ": "Horned dung beetle",
    "What is the capital of France?": "paris",
    "What is the capital of Germany?": "berlin",
    "What is the capital of Italy?": "rome",
    "What is the capital of Spain?": "madrid",
    "What is the second largest country in the world?": "canada",
    "Where is the largest desert in the world?": "antarctica",
    "What country has the most geyser activity?": "iceland",
    "What year  did the berlin wall fall?": "1989",
    "In Romeo and Juliet, what is the name of the family that the two lovers belong to?": "montague",
    "What is the name of the main character in the book The Hobbit?": "bilbo",
    "What is the name of the main character in the book The Lord of the Rings?": "frodo",
    "What is the name of the main character in the book The Chronicles of Narnia?": "aslan",
    "What is the name of the main character in the book The Lion, the Witch and the Wardrobe?": "edmund",
    "What is the monkeys name in Lion King?": "rafiki",
    "What year did the Berlin congress take place?": "1878",
    "What year did the Treaty of Versailles take place?": "1919",
    "What year did the French Revolution take place?": "1789",
    "What year did the first World Cup take place?": "1930",
    "Who was the last Roman Emperor?": "romulus augustus",
    "Where did Napoleon exile himself to?": "elba",
    "Who wrote The Art of War?": "sun tzu",
    "Who won the NBA championship in 2016?": "cleveland cavaliers",
    "Who won the NBA championship in 2015?": "golden state warriors",
    "Who won the Champions League in Istanbul in 2005?": "liverpool",
    "What is the capital of Brazil?": "Brasília",
    "What is the capital of Russia?": "Moscow",
    "What is the capital of Egypt?": "Cairo",
    "What is the capital of Australia?": "Canberra",
    "What is the capital of Japan?": "Tokyo",
    "What is the capital of Indonesia?": "Jakarta",
    "What is the capital of South Africa?": "Johannesburg",
    "What is the capital of Canada?": "Ottawa",
    "What is the capital of Chile?": "Santiago",
    "What is the capital of Pakistan?": "Islamabad",
    "What is the element with the atomic number 1?": "Hydrogen",
    'Which planet is known as the "Red Planet"?': "Mars",
    "What is the name of the largest ocean in the world?": "Pacific Ocean",
    'Who wrote the novel "One Hundred Years of Solitude"?': "Gabriel Garcia Marquez",
    "What is the currency of China?": "Yuan",
    "What is the largest mammal in the world?": "Blue Whale",
    "What is the name of the smallest country in the world by land area?": "Vatican City",
    "What is the name of the process of converting sunlight into electricity?": "Photovoltaics",
    "Which element is the most abundant in the earth's crust?": "Oxygen",
    'Which planet is known as the "Ice Giant"?': "Uranus",
    "What is the name of the most famous sculpture by Michelangelo?": "David",
    "What is the currency of the United Kingdom?": "Pound",
    'Which country is known as the "Land of the Rising Sun"?': "Japan",
    "What is the largest bird in the world?": "Ostrich",
    "What is the name of the smallest country in the world by population?": "Vatican City",
    "What is the name of the process of producing electricity by harnessing the kinetic energy of water?": "Hydroelectric Power",
}

SECOND_GAME_QUESTIONS = {
    "Who wrote Catch-22": ["joseph heller", "mark twain", "james joyce"],
    "What is the name of the main character in Pride and Prejudice?": [
        "elizabeth bennet",
        "darcy bennet",
        "jane bennet",
    ],
    "Where is the Brandenburg Gate?": ["berlin", "munich", "hamburg"],

    "Who invented the telephone?": ["alexander graham bell", "thomas edison", "steve jobs"],
    "Who invented the light bulb?": ["nikola tesla", "alexander graham bell", "thomas edison"],
    "Who invented the computer?": ["alan turing", "charles babbage", "steve jobs"],
    "Who invented the airplane?": ["the wright brothers", "charles babbage", "steve jobs"],
    "What is the name of Ford's founder?": ["henry ford", "john ford", "george ford"],
    "What does GMC stand for?": ["general motors corporation", "general motors company", "general motors corporation"],
    "When did the Spanish flu pandemic start?": ["1918", "1920", "1922"],
    "When did the first world war start?": ["1914", "1918", "1920"],
    "When did the second world war start?": ["1939", "1940", "1941"],
    "When did the Bosnian war start?": ["1992", "1993", "1994"],
    "When did the Vietnam war start?": ["1955", "1960", "1965"],
    "When did the Korean war start?": ["1950", "1955", "1960"],
    "When did the Cuban missile crisis start?": ["1962", "1963", "1964"],
    "When did the first moon landing take place?": ["1969", "1970", "1971"],
    "Who killed John F. Kennedy?": ["lee harvey oswald", "lee henry", "al capone"],
    "Who killed Abraham Lincoln?": ["john wilkes booth", "frederic hopkins", "enero garcia"],
    "What year did Michael Jackson die?": ["2009", "2010", "2011"],
    "What year did Elvis Presley die?": ["1977", "1978", "1979"],
    "What year did John Lennon die?": ["1980", "1981", "1982"],
    "What is the typical current in a household socket?": ["220 volts", "110 volts", "240 volts"],
    "What is the typical current in a car battery?": ["12 volts", "24 volts", "36 volts"],
    "What is the eye doctor called?": ["ophthalmologist", "oronthalmologist", "ophthalogist"],
    "What animal is the symbol of the United Nations?": ["elephant", "lion", "tiger"],
    "What was the name of the first computer?": ["eniac", "atari", "apple"],
    "How many legs does a spider have?": ["eight", "six", "ten"],
    "How many legs does a bee have?": ["six", "eight", "ten"],
    "How many legs does a butterfly have?": ["six", "eight", "ten"],
    "What is the largest lizard in the world?": ["giant lizard", "komodo dragon", "african cameleon"],
    "Where was Jesus born?": ["bethlehem", "nazareth", "jerusalem"],
    "What country hosted the 1984 Winter Olympics?": ["yugoslavia", "germany", "italy"],
    "When did the first Winter Olympics take place?": ["1924", "1928", "1932"],
    "John F. Kennedy was assassinated in which city?": ["dallas", "houston", "austin"],
    "Paul McCartney was a member of which band?": ["the beatles", "the rolling stones", "the doors"],
    "On which continent is the country of Australia?": ["oceania", "asia", "africa"],
    "Pablo Picasso was a famous painter from which country?": ["spain", "france", "italy"],
    "Karl Marx was a famous philosopher from which country?": ["germany", "france", "italy"],
    "Leonardo da Vinci was a famous painter from which country?": ["italy", "france", "germany"],
    "Charles Darwin was a famous scientist from which country?": ["england", "france", "germany"],
    "Ziggy Stardust was a famous musician from which country?": ["england", "france", "germany"],
    "How many sides does a hexagon have?": ["six", "eight", "ten"],
    "Galileo Galilei was a famous scientist from which country?": ["italy", "france", "germany"],
    "Aragorn was king of which kingdom in the Lord of the Rings?": ["gondor", "mordor", "rohan"],
    "Frodo was a hobbit from which kingdom in the Lord of the Rings?": ["shire", "mordor", "rohan"],
    "What is the name of the main character in The Great Gatsby?": [
        "nick carraway",
        "jordan baker",
        "daisy buchanan",
    ],
    "What is the name of the main character in The Catcher in the Rye?": [
        "holden caulfield",
        "phoebe caulfield",
        "allie caulfield",
    ],
    "Which country does not share a border with Romania?": [
        "poland",
        "ukraine",
        "hungary",
    ],
    "Which artist and author made the Smurfs comic strips?": ["peyo", "peter", "paul"],
    "How many wives did Henry VIII have?": ["six", "seven", "eight"],
    "When did Salt Lake City host the Winter Olympics?": ["2002", "2006", "2010"],
    "In which city can you find the Prado Museum?": ["madrid", "barcelona", "valencia"],
    "When was the book “To Kill a Mockingbird” by Harper Lee published?": [
        "1960",
        "1962",
        "1964",
    ],
    'Who wrote the novel "War and Peace"?': [
        "Leo Tolstoy",
        "Fyodor Dostoevsky",
        "Anton Chekhov",
    ],
    "What is the capital of the Republic of Yemen?": ["Sana'a", "Aden", "Taizz"],
    "What is the name of the most massive star known to exist?": [
        "R136a1",
        "RW Cephei",
        "UY Scuti",
    ],
    'Who wrote the short story "The Masque of the Red Death"?': [
        "Edgar Allan Poe",
        "H.P. Lovecraft",
        "Nathaniel Hawthorne",
    ],
    'Who composed the famous opera "The Magic Flute"?': [
        "Wolfgang Amadeus Mozart",
        "Ludwig van Beethoven",
        "Giacomo Puccini",
    ],
    "What is the largest organ in the human body by weight?": [
        "Liver",
        "Skin",
        "Heart",
    ],
    "What is the highest mountain peak on Earth?": [
        "Mount Everest",
        "K2",
        "Mount Denali",
    ],
    'Who wrote the famous play "A Streetcar Named Desire"?': [
        "Tennessee Williams",
        "Eugene O'Neill",
        "Arthur Miller",
    ],
    "What is the most abundant element in the earth's atmosphere?": [
        "Nitrogen",
        "Oxygen",
        "Carbon Dioxide",
    ],
    "What is the capital of the Republic of Chad?": ["N'Djamena", "Abéché", "Moundou"],
    "What is the name of the process of converting sunlight into electricity?": [
        "Photovoltaics",
        "Nuclear Fusion",
        "Nuclear Fission",
    ],
    'Who wrote the famous opera "The Barber of Seville"?': [
        "Gioachino Rossini",
        "Wolfgang Amadeus Mozart",
        "Vincenzo Bellini",
    ],
    "What is the name of the most massive planet in our solar system?": [
        "Jupiter",
        "Saturn",
        "Neptune",
    ],
    'Who wrote the novel "The Picture of Dorian Gray"?': [
        "Oscar Wilde",
        "William Butler Yeats",
        "W.B. Yeats",
    ],
    "What is the name of the famous painting depicting the French Revolution beheading of King Louis XVI": [
        "The Death of Marat",
        "The Death of Louis XVI",
        "The Reign of Terror",
    ],
    'Who wrote the famous play "Hamlet"?': [
        "William Shakespeare",
        "Christopher Marlowe",
        "Ben Jonson",
    ],
    "What is the name of the largest mammal in the world?": [
        "Blue Whale",
        "Elephant",
        "Giraffe",
    ],
    "What is the name of the smallest country in the world by land area?": [
        "Vatican City",
        "Monaco",
        "Nauru",
    ],
}

THIRD_GAME_QUESTIONS = {
    "What is Garabogazk'l?" : " Lagoon",
    "How many countries in Africa have only four letters in their names?" : "Three",
    "Which country has its UN code 328?" : "Guyana",
    "Which process converts sugar to acids, alcohol, or gases?" : "Fermentation",
    "What state has the letter Z in it?" : "Arizona",
    "Henrik Carl Peter Dam and Edward Adelbert Doisy received the Nobel Prize in Physiology or Medicine in which year?" : "1943",
    "What letter isn't in any US state?" : "Q",
    "What is Africa's original name?" : "Alkebulan",
    "How many victims died due to lack of sleep in Shakespeare's plays?" : "One",
    "Stratification of a body of water due to salinity differences is called what?" : "Halocline",
    "What is the only country beginning with O?" : "Oman",
    "Enchiladas originated in which country?" : "Mexico",
    "To the nearest thousand, how many words are in the complete works of Shakespeare?" : "884,000",
    "Where did the Duke and Duchess of Windsor visit in 1937, later causing controversy for the royal family?" : "Berlin",
    "What European nation holds a Four Letter nation in its letters?" : "Eire",
    "What letter do most US states begin with?" : "M",
    "What is the capital of Hawaii?" : "Honolulu",
    "In Dirty Dancing, what is Baby's first name?" : "Frances",
    "Johannes Vilhelm Jensen received the Nobel Prize in 1944 in which category?" : "Literature",
    "Organism that thrives in high salt concentrations is called what?" : "Halophile",
    "Which country end with a WAY?" : "Norway",
    "What is a technical term for the legendary first people of any creation myth, including a list of first men and women in different traditions?" : "Protoplasts",
    "In which Welsh town did a young Prince Charles learn Welsh?" : "Aberystwyth",
    "The first woman to win an Olympic gold medal, Charlotte Cooper is from which country?" : "England",
    "How many countries start and end with the same letter?" : "Six",
    "SInce inception, how many times the Nobel Prizes have not been awarded as of 2021?" : "49",
    "Which Disney Princess called Gus and Jaq friends?" : "Cinderella",
    "What is the biggest state in America?" : "Alaska",
    "In which country would you find the original Legoland?" : "Denmark",
    "How many minutes long is the film Jaws?" : "124",
    "How many states have 5 letters?" : "3",
    "Between 1901 and 2020, the Nobel Prizes and the Prize in Economic Sciences were awarded how many times?" : "603",
    "What is the internet country domain TLD for Ghana?" : " gh",
    "Joseph Erlanger and Herbert Spencer Gasser received the Nobel Prize in Physiology or Medicine in which year?" : "1944",
    "What percentage of the Earth's surface is made up o the Atlantic Ocean?" : "20%",
    "In which sport would you use a shuttlecock?" : "Badminton",
    "How many American states start with new?" : "4",
    "What kind of food is Penne?" : "Pasta",
    "Otto Stern received the Nobel Prize in 1943 in which category?" : "Physics",
    "In which state was former US President Barack Obama born?" : "Hawaii",
    "How many teeth does an adult human have?" : "32",
    "To the nearest day, how many days in total with Elizabeth's uncle's reign as Edward VIII before he abdicated?" : " 326",
    "In Welsh mythology, who is a metalsmith considered to be, like the Irish Goibniu, a reflex of the Gallo-Roman deity Gobannus?" : "Gofannon",
    "How high is Mount Everest in meters?" : "8848",
    "Which country ends with ANY?" : "Germany",
    "What is a stringed musical instrument in traditional Japanese theater meaning 'three-flavor line string'?" : "Shamisen",
    "What year did Britain join the EEC, now knows as the European Union?" : "1973",
    "What is an elegant brand, Hermes?" : "Jewelry",
    "Which Friend has the middle name, Muriel?" : "Chandler",
    "What is a nation on the Red Sea?" : "Eritrea",
    "In which year, at St  Mary's Hospital, London, Alexander Fleming discovered penicillin?" : "1928",
    "Which country ends with a MEN?" : "Yemen",
    "What is the Alpha 2 code for Ghana?" : "GH",
    "Which character is often referred to with 'Giantsbane' in their name in the Game of Thrones?" : "Tormund",
    "Which location has its internet country domain TLD  gi?" : "Gibraltar",
    "What kind of Japanese brand 6%DokiDoki is?" : "Cloth",
    "Gocta, Catarata falls is where in Peru?" : "Amazonas",
    "What weird food in Ukrain is meaty jello with garlic and pieces of said meat inside?" : "Kholodets",
    "How many countries start with an A?" : "Eleven",
    "What color are the seats in the House of Commons?" : "Green",
    "Slovakia's capital is what?" : "Bratislava",
    "According to statistics, what percent of Americans lose their wallets/purses?" : "20%",
    "Which country has its Alpha 2 code GH?" : "Gibraltar",
    "What is Breezy in Japan?" : "Dress",
    "Famous novel Crash was written in which year?" : "1973",
    "Which color is commonly associated with Marie Schrader throughout the show in Breaking Bad?" : "Purple",
    "What is the UPC barcode for Pakistan?" : "896",
    "How did Italian composer Giacomo Puccini die?" : "Cancer",
    "Which country ends with a VIA?" : "Latvia",
    "Beaver (Castor sp ) has its average gestation period of how many days?" : "122",
    "What is a suburb of Kumasi in the Ashanti Region of Ghana?" : "Ashtown",
    "In which year Arnold Schwarzenegger received the Doctor of Humane Letters for contribution?" : "1996",
    "What is the Alpha 3 code for Grenada?" : "GRD",
    "The science concerned with the origin, evolution, and structure of the earth is called what?" : "Geology",
    "Who is the god of doors, time, duality, doorways, passages, frames, transition, and gates in Roman mythology?" : "Janus",
    "Which famous novel Sinclair Lewis wrote in 1922?" : "Babbitt",
    "In which year, Arnold Schwarzenegger won Nickelodeon Kids' Choice Awards for 'Terminator 2: Judgement Day'?" : "1992",
    "Neutral litmus paper is what color?" : "Purple",
    "Ashburys Railway Station is located in which city?" : "Manchester",
    "Khaan Buuz is a brand in which country?" : "Mongolia",
    "What is the capital of Bulgaria?" : "Sofia",
    "How many episodes of Breaking Bad were aired?" : "62",
    "Which country has its Alpha 3 code GP?" : "Guadeloupe",
    "What is a Laffy Taffy?" : "Candy",
    "What special character can be get from the shortcut keys Alt+0246?" : "'",
    "What is JAR Bolt of Lightning?" : "Perfume",
    "Peugeot is originated in which country?" : "France",
    "In which century did Rembrandt live?" : "17th",
    "What is a time period when sacrifices were made to atone for sins?" : "Februalia",
    "Ammonia gas turns red litmus paper what color?" : "Blue",
    "What color shirt is Walt wearing in the iconic desert scene where he is pointing a gun wearing his white underwear, in Breaking Bad?" : "Green",
    "What is the national flower in Portugal?" : "Lavender",
    "What is the UN Code for Haiti?" : "332",
    "A Croatian speaks in what language?" : "Croatian",
    "What is the generic name for any chemical product that is used industrially and domestically to remove color from a fabric or fiber or to clean or to remove stains?" : "Bleach",
    "Riboflavin was discovered in what year?" : "1920",
    "Rush Lake is located in which county in Utah?" : "Tooele",
    "What is the brand Red Vines loved by children?" : "Candy",
    "What is the capital of Pakistan?": "Islamabad",
    "Where was the Bosnian War peace agreement signed?": "Dayton",
    "How many bones are in the human body?": "206",
    "What is the formula for Hydrogen Peroxide?": "H2O2",
    "What is the name of the largest ocean in the world?": "Pacific",
    "What is the name of the brightest star in the sky?": "Sirius",
    "How many species of sharks are there?": "500",
    "Where was Alexander the Great born?": "Macedonia",
    "When was Joan of Arc burned at the stake?": "1431",
    "When was Julius Caesar assassinated?": "44 BC",
    "What is the name of the stone that helped people decipher Egyptian hieroglyphics?": "Rosetta Stone",
    "Where did the first Olympic Games take place?": "Greece",
    "What was the biggest empire in history?": "Mongol Empire",
    "What Croat general held off the Ottomans": "Zrinski",
    "What European city has the most Champions League and Euroleague titles?": "Madrid",
    "Who won the 1991 NBA Finals?": "Chicago Bulls",
    "How many NBA championships does Kobe Bryant have?": "5",
    "Who won the 2019 NBA Finals?": "Toronto Raptors",
    "Who was the first player to score 100 points in a single NBA game?": "Wilt Chamberlain",
    "Who directed the Hatefull Eight?": "Quentin Tarantino",
    "Who directed the movie The Godfather?": "Francis Ford Coppola",
    "Who directed the movie The Shawshank Redemption?": "Frank Darabont",
    "Who directed the movie Pulp Fiction?": "Quentin Tarantino",
    "Who directed the movie The Dark Knight?": "Christopher Nolan",
    "Who played the role of Neo in the Matrix?": "Keanu Reeves",
    "Who played the role of Scully in the X-Files?": "Gillian Anderson",
    "Who played the role of Agent Cooper in Twin Peaks?": "Kyle MacLachlan",
    "Who played the role of Agent Mulder in the X-Files?": "David Duchovny",
    "Who played the role of Agent Smith in the Matrix?": "Hugo Weaving",
    "Who played the Joker in the Dark Knight?": "Heath Ledger",
    "How high is Mount Everest?": "8848",
    "How high is Mount Kilimanjaro?": "5895",
    "Where is Mount Everest located?": "Nepal",
    "Where is Mount Kilimanjaro located?": "Tanzania",
    "How many bones are in the human body?": "206",
    "How many bones are in the human hand?": "27",
    "What is the longest bone in the human body?": "Femur",
    "What did Alfred Nobel invent?": "Tnt",
    "What was the project named that dropped the atomic bomb on Hiroshima?": "Manhattan Project",
    "What is the position of Nitrogen in the periodic table?": "7",
    "What is the position of Oxygen in the periodic table?": "8",
    "What is the population of the United States in millions?": "328",
    "What is the population of China in billions?": "1.4",
    "What is the population of India in billions?": "1.3",
    "How many countries are in the EU?": "28",
    "Where did Holodomor take place?": "Ukraine",
    "Who caused the Holodomor?": "Stalin",
    "What world famous Techno club is located in Berlin?": "Berghain",
    "What is the name of the famous Techno club in Tbilisi?": "Bassiani",
    "What is the name of the famous Techno club in London?": "Fabric",
    "How many islands does Croatia have?": "1183",
    "How many seasons did Michael Jordan play in the NBA?": "15",
    "How many seasons did Kobe Bryant play in the NBA?": "20",
}

totalMoney = []
totalMoneyAfterSecondGame = []

def handle_input(prompt, default_value):
    try:
        return int(input(prompt))
    except IndexError:
        return default_value


print("\tWelcome to The Chase!")
print(
    "\n1️⃣  In the first game, you have 60 seconds to answer as many questions as possible."
)
print("Correct answers are worth $500. 💸\n")
print("2️⃣  In the second game, you can choose your head start from the hunter.")
print("If caught, the game is over. 🛑\n")
print(
    "3️⃣  In the third game, you have 120 seconds to answer as many questions as possible."
)
print("Each question is worth 1 point. 🧠")
print("To win, you must have more points than the hunter.")
print("If the hunter is incorrect, you can take him back a step.")

start = input("\n\tStart the game? (yes/no) ")


def get_random_question():
    """Returns a random question and answer from the dictionary."""
    question, answer = random.choice(list(FLASH_QUESTIONS.items()))
    return question, answer


def get_random_question2():
    """Returns a random question and answer from the dictionary for the second game."""
    question, answer = random.choice(list(SECOND_GAME_QUESTIONS.items()))
    return question, answer


def get_random_question3():
    """Returns a random question and answer from the dictionary for the third game."""
    question, answer = random.choice(list(THIRD_GAME_QUESTIONS.items()))
    return question, answer


def main():
    """The first game of the show."""
    start_time = time.time()
    end_time = start_time + 60
    money = 0
    used_questions = ()
    print("Press enter to pass the question")


    while time.time() < end_time:
        time.sleep(1)
        question, answer = get_random_question()
        while question in used_questions:
            question, answer = get_random_question()
        used_questions += (question,)
        print(f"\n{question}")

        user_answer = input("Your answer: ").lower()


        if user_answer == answer.lower():
            print("\n\tCorrect!✅")
            money += 500
            print("\nTime remaining: {} seconds".format(int(end_time - time.time())))
            totalMoney.append(500)

        else:
            print("\n\tIncorrect!❌")
            print("\nTime remaining: {} seconds".format(int(end_time - time.time())))
            continue

        print("You take ${} to the next round".format(money))
        print("---------------------")

    print("Higher offer will give you a 2 place head start.")
    print("Middle offer will give you a 3 place head start.")
    print("Lower offer will give you a 4 place head start.")

    time.sleep(1)

    print("\n\t💵 Choose your offer 💵")

    """The second game of the show."""
    higher_offer = sum(totalMoney) + (sum(totalMoney) * 2.86)
    medium_offer = sum(totalMoney)
    lower_offer = sum(totalMoney) - (sum(totalMoney) * 0.86)
    totalMoneyAfterSecondGame
    print("\n1.) The higher offer is: {}$".format(higher_offer))
    print("\n2.) The middle offer is: {}$".format(medium_offer))
    print("\n3.) The lower offer is: {}$".format(lower_offer))
    offer_selected = input("\nYour choice: ")

    if offer_selected == "1" or offer_selected == "higher":
        head_start = 2
        totalMoneyAfterSecondGame.append(higher_offer)
        print("\nYou have chosen the higher offer!")
    elif offer_selected == "2" or offer_selected == "middle":
        head_start = 3
        totalMoneyAfterSecondGame.append(medium_offer)
        print("\nYou have chosen the medium offer!")
    elif offer_selected == "3" or offer_selected == "lower":
        head_start = 4
        totalMoneyAfterSecondGame.append(lower_offer)
        print("\nYou have chosen the lower offer!")

    correct_answers = 0
    counter = 0
    used_questions = set()
    question_keys = list(SECOND_GAME_QUESTIONS.keys())
    random.shuffle(question_keys)

    while head_start > 0 and counter < 6:

        for question_key in question_keys:
            if question_key in used_questions:
                continue
            if counter >= 6 or head_start <= 0:
                break
            question = question_key
            alternatives = SECOND_GAME_QUESTIONS[question_key]
            correct_answer = alternatives[0]
            random.shuffle(alternatives)
            print(f"\n{question}")
            for idx, alternative in enumerate(alternatives):
                print(f"{chr(97 + idx)}) {alternative}")
            answer_letter = input("Answer: ").lower()
            answer = alternatives[ord(answer_letter) - ord("a")]
            if answer == correct_answer:
                print("\n\tCorrect! ✅")
                correct_answers += 1
                counter += 1
                print(f"\nYou are {head_start} places ahead of the Hunter")
            else:
                print(f"❌ The answer is {correct_answer!r}, not {answer!r}")
                kresimir_correct = random.randint(0, 100)
                if kresimir_correct < 80:
                    print("\tHunter is correct!")
                    head_start -= 1
                    print(f"\n\tYou are {head_start} places ahead of the Hunter")
                else:
                    print("\tHunter is incorrect!")
                    print(f"\n\tYou are {head_start} places ahead of the Hunter")
                    continue
        if counter == 6:
            print("You move on to the next game!")
            break
        if head_start <= 0:
            print("You lost the game!")
            return
    time.sleep(3)
    print("Get ready for the final game")
    """The third game of the show."""
    print("You have ${} in the bank".format(sum(totalMoneyAfterSecondGame)))
    print("Your 120 seconds start now!")
    start_time = time.time()
    end_time = start_time + 120
    correct_answers = 0
    used_questions = set()

    while time.time() < end_time:
        for question_key in question_keys:
            if question_key in used_questions:
                continue

        time.sleep(2)

        question, answer = get_random_question3()
        print(f"\n{question}")
        

        user_answer = input("Your answer: ").lower()
        if user_answer == answer.lower():
            print("\n\tCorrect!✅")
            correct_answers += 1
            print("\nTime remaining: {} seconds".format(int(end_time - time.time())))
            print(f"You have {correct_answers} correct answers")
        else:
            print("\n\tIncorrect!❌")
            print("\nTime remaining: {} seconds".format(int(end_time - time.time())))
            continue

    # After the player finishes answering questions
    hunters_correct_answers = 0
    for i in range(25):
        time.sleep(1)
        hunter_correct_answer_range = random.randint(0, 100)
        if hunter_correct_answer_range < 75:
            time.sleep(1)
            print("\nHunter is correct!")
            hunters_correct_answers += 1
            print(f"\n\tHunter has {hunters_correct_answers} correct answers")
        else:
            time.sleep(1)
            print("\nHunter is incorrect!")
            question, answer = get_random_question3()
            print(f"\n{question}")
            user_answer = input("Your answer: ").lower()
            if user_answer == answer.lower():
                print("\n\tCorrect!✅")
                hunters_correct_answers -= 1
                print(f"\nHunter has {hunters_correct_answers} correct answers")
            else:
                print("\n\tIncorrect!❌")
                continue

    if hunters_correct_answers > correct_answers:
        print("\nYou lost the game!")
    else:
        print("\nYou won the game!")
        print(
            "\nCongratulations! You have won ${}".format(sum(totalMoneyAfterSecondGame))
        )

    play_again = input("\nDo you want to play again? ").lower()
    if play_again == "yes":
        main()


if __name__ == "__main__":
    if start == "yes":
        main()
