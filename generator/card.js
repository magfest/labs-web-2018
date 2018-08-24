// Extremely quick and dirty card generator - generates the html for cards so it's harder to mess up.
// Build using nodejs 8+
// Just run as `node ./card.js` ... comment in/out the cards below based on the section you want to re-generate. 
// Would've been nicer to create something to generate the entire html pages, but, meh...

function getCard(name, link, image, text) {
    var linkHtml = name;
    if (link !== null) {
        linkHtml = '<a href="' + link + '">' + name + '</a>';
    }
    return `
<div class="col-md">
    <div class="card">
        <div class="card-block">
            <img src="${image}" alt="${name}" class="card-img-top" />
            <div id="content">
                <h3 class="card-title">${linkHtml}</h3>
                <p class="card-text">${text}</p>
            </div>
        </div>
    </div>
</div>
    `;
}

var html = '',
    i = 0;

var all = [
    /*
    // Play START
    ['Console Room', null, 'https://images.pexels.com/photos/776092/pexels-photo-776092.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260', 'MAGLabs hosts dozens upon dozens of consoles, ranging from the NES up through everything modern. And don\'t worry; we have all the party games!'],
    ['Arcade', null, 'https://images.pexels.com/photos/374914/pexels-photo-374914.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260', 'MAGLabs hosts an exciting arcade with many of your old favorites. Come play with your friends!' ],
    ['LAN', null, 'https://images.pexels.com/photos/735911/pexels-photo-735911.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260', 'More of a computer gamer? MAGLabs has a room dedicated to lan parties! We also host a number of tournaments throughout the weekend!'],
    ['Tabletop', null, 'play.jpg', 'MAGLabs knows tabletop games. From popular games like Settlers of Catan, to the much more complex and obscure, you can find players. The event also has many games for rental!'],
*/

    // Play END

    // Create START
/*
    ['Gamer Iron Chef', 'https://docs.google.com/forms/d/e/1FAIpQLSdNDZCJQA5HCDCsLyrDDoAgY18s_tppzhdDHQ3q8Eiu9k9UpA/viewform', 'https://lh6.googleusercontent.com/HMgX3uIYAED_KgoStZUSUFhP3bvFFtofDCT2I-F8KcoVDxAFxQXzG6-z8xKz7Erweyuso7SWFw=w1595', 'Three teams of three will battle it out to see who is the ultimate Gamer Iron Chef! Teams will have 1 hour to prepare an appetizer, main course and either a dessert or beverage.  In true Iron Chef style, several mystery ingredients will be revealed at the beginning of the contest that must be incorporated into each team\'s dishes. '],
*/
    // Create END

    // Learn START

    ['Wes Johnson', 'https://www.facebook.com/wesjohnsonvoice', 'https://scontent.fbed1-1.fna.fbcdn.net/v/t1.0-9/38391403_10156558771587937_9127940187114962944_o.jpg?_nc_cat=0&amp;oh=275177b751f6ac0f22bde2c700d878fa&amp;oe=5C32CC64', "I'm sure a lot of you are thinking... Where are literally ANY of the guests this year? Well, we just haven't announced them yet! Let's fix that, starting now. Please welcome back a man of seemingly infinite voices, Wes Johnson! When he isn't rocking the red with the Washington Capitals as their stadium announcer, he's filling a voice role for Bethesda, Blizzard, or countless other projects. Wes goes by many other names: Sheogorath. Lucien Lachance. The Silver Shroud. Fawkes. Moe Cronin. Herameus Mora. He was both the Criminal Scum and the Guards who arrested them! Wes was EVERY Protectron robot, Mr Burke, and Scribe Bigsley. He was in a John Waters film. The man was in The Wire! It's hard to think of things he HASN'T appeared in."],
    ['Kevin Ryan', null, 'https://scontent.fbed1-1.fna.fbcdn.net/v/t1.0-9/38485827_10156568859587937_7538990720695140352_n.jpg?_nc_cat=0&amp;oh=5de5c66c66fac7c7931cadb02934c69c&amp;oe=5BFCE26C', "Now residing high up in the Sierra Nevada mountains with his wife and kids, Kevin got his start making games 40 years ago on an 8 KB computer. He was one of the owners of Dynamix and worked on many projects including Arctic Fox, which was the first original game for the Amiga computer. He is the original designer and programmer of The Incredible Machine! A few of his other games are Skyfox II, F-14 Tomcat, Heart of China, Rise of the Dragon, 3D Ultra Minigolf, Marble Blast, and most recently, Contraption Maker. They were published by various acclaimed companies including Electronic Arts, Activision, and Sierra! When he isn't coding, Kevin gets his wintry workouts in the form of snow shoveling, and homebrews his own ale all year round!"],
    ['Jon Bolding', 'https://twitter.comJonBolds', 'https://scontent.fbed1-1.fna.fbcdn.net/v/t1.0-9/38756601_10156574037077937_6487797792826720256_n.jpg?_nc_cat=0&amp;oh=8d97cf08e45465750f1c892d84caa6a9&amp;oe=5C0158EF', 'Jon Bolding has made the admittedly questionable decision of spending his adult life writing about video and tabletop games, and now to hang out with us at #MAGLabs2018! Are you hype yet?'],
    ['Dr. Corey Olsen', null, 'https://scontent.fbed1-1.fna.fbcdn.net/v/t1.0-9/39227302_10156584099057937_96609022966235136_n.jpg?_nc_cat=0&amp;oh=5e27bd72b585bbd5febafff0e2e11eb9&amp;oe=5BF8BE1E', 'Dr. Corey Olsen is the President of Signum University and Mythgard Institute. In addition to teaching classes on J.R.R. Tolkien, Chaucer, and modern fantasy literature for Signum, Dr. Olsen has extended the concept of the digital classroom to include non-traditional outlets. Through the Mythgard Academy, he offers free weekly lectures on works of speculative fiction chosen by Signum University supporters, and he has embraced the “new literature” of cinema and video game adaptations through interactive programs such as The Silmarillion Film Project and in-game discussions of Lord of the Rings Online.'],
    ['Steven S. Long', 'http://www.stevenslong.com', 'https://scontent.fbed1-1.fna.fbcdn.net/v/t1.0-9/39171338_10156586605452937_5877838370083700736_n.jpg?_nc_cat=0&amp;oh=74f71f3d61632127c8f8b4daac199231&amp;oe=5BF61DF1', "Steven S. Long is a writer and game designer who has worked primarily in the tabletop roleplaying game field for the past twenty-five years. During that time, Steven has written or co-written approximately 200 RPG books. He's best known for his work with Champions and the HERO System, but has worked with many other RPG companies including Last Unicorn Games, Pinnacle Entertainment Group, Decipher, and White Wolf. In recent years, Steve branched out into writing fiction as well, and his first major work of non-fiction, a book on the Norse god Odin for Osprey Publishing, was released in May 2015. His Master Plan for World Domination has reached Stage 72-Delta."],
    ['Ryan Amon', null, 'https://scontent.fbed1-1.fna.fbcdn.net/v/t1.0-9/37500455_10156590913377937_6853858430990417920_n.jpg?_nc_cat=0&amp;oh=2f2fdb14b617045eb36197a80fb107a9&amp;oe=5BF565DE', " Ryan Amon is an American composer born in Elkhorn, Wisconsin, where he began composing music at an early age with a background in classical piano and saxophone. He has worked as a ghostwriter and library music composer for many TV shows including American Idol, The Oprah Winfrey Show, and Dancing with the Stars. Time spent in Bolivia eventually inspired Ryan to form the motion picture advertising company ‘City of the Fallen’ in 2009. City of the Fallen's music has been featured in the trailers for many movies, including Marvel's \"The Avengers\". Ryan has also branched into the video game world, composing music for both FromSoftware's 'Bloodborne' and Ubisoft's 'Assassin's Creed: Unity'. In the fall of 2015, the world premiere suite of his themes from Bloodborne was performed live in concert in Stockholm, Sweden."],
    ['Mike Rosson', null, 'https://scontent.fbed1-1.fna.fbcdn.net/v/t1.0-9/39441826_10156593675132937_6397416584108834816_n.jpg?_nc_cat=0&amp;oh=5b2c42c02513e9fd2565089d6f4ccba8&amp;oe=5BF61AD3', "A mirthful, piratical lad, Mike Rosson is an endless font of fun voices and outrageous humor. Mike's vocal versatility has served him well in games, as he ruled the wastelands in FALLOUT 4 as the Minuteman Radio Voice and the Vault Tech Scientist, and in FALLOUT 3 as Colin Moriaty, Dr Lesko, Gob and all male Ghouls. Mike took to space and battled all five legendary original Starfleet Captains as various Klingons, Romulans, Cardassians and Borg in Star Trek: Legacy & Star Trek Conquest. Visually, he has appeared in films such as John Waters' 'A Dirty Shame' and the cult classic 'The Better Half'."],
    ['Edmund "Ed" Habib', null, 'https://scontent.fbed1-1.fna.fbcdn.net/v/t1.0-9/39742514_10156600822532937_8583939977295953920_o.jpg?_nc_cat=0&amp;oh=8b311a27304c3d082472499d385dcabe&amp;oe=5BF77391', 'Edmund "Ed" Habib is a pre-Apollo rocket engineer. At 92, his career isn\'t over, as he\'s still being called on by the head of NASA. Vangaurd; TDRS; GPS; V2; Viking; Aerobee; Minitrack Tracking system... you name it, he built it; invented it; or payload managed it. As the Branch Head of Goddard, he designed and built Goddard\'s data-centers, which are responsible for converting streams of analog satelite data into digital format.'],
    ['Meg Eden', 'http://megedenbooks.com', 'https://static1.squarespace.com/static/549c3030e4b0d2e1e2094357/549c32ede4b0f044366b34e7/5b3bed2970a6ade9f6a12fa2/1530654000074/awesomecon182.png?format=500w', 'Meg Eden teaches creative writing at Anne Arundel Community College. She has five poetry chapbooks, and her novel "Post-High School Reality Quest" is published with California Coldblood, an imprint of Rare Bird Books. Find her online at <a href="http://www.megedenbooks.com">www.megedenbooks.com</a> or on Twitter at @ConfusedNarwhal'],

    // Learn END


//     ['Event Name', 'https://event.event', 'http://image.image', 'This is a card about this event']
];

all.forEach(function() {
    console.info('row ' + i);
    if (i % 4 == 0) {
        html += '<div class="row">';
    }
    html += getCard(all[i][0], all[i][1], all[i][2], all[i][3]);
    if (i % 4 == 3 || i == all.length-1) {
        html += '\n</div>';
    }
    i++;
});

console.info(html);