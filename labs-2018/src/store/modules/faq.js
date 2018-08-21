// set up faq data
const state = {
  questions: [
    {
      question: 'Will MagLabs be selling one day badges this year?',
      answer: 'We will be selling one-day badges for the following prices: <ul><li>Friday: $25</li><li>Saturday: $35</li><li>Sunday: $15</li></ul> One day badges run from 12:00 AM to the next day at 6:00 AM, so 12:00 AM Saturday to 6:00 AM Sunday.',
      note: 'Please note: You will not able to pick up your badge before the start time for the day of the badge.'
    },
    {
      question: 'I BOUGHT A ONE DAY BADGE AND DECIDED I WANT TO STAY THE WHOLE WEEKEND. HOW DO I UPGRADE?',
      answer: 'You may return your one day badge to Registration and upgrade to a full weekend badge by paying the difference between the two badges. Your one day badge must be relinquished at the time of upgrade as an individual can only have one badge at a time.'
    },
    {
      question: 'HOW DO I SELL OR TRANSFER MY BADGE?',
      answer: 'To transfer your registration to another person, open your confirmation email and send them the personalized link referenced in the last paragraph. Please note: You may resell your registration for no more than the exact price you paid for it.',
      note: 'Warning: If you purchased an upgrade tier with your badge that will also be transferred when your badge is transferred.'
    },
    {
      question: 'I AM UNABLE TO FIND MY PREREGISTRATION EMAIL. CAN IT BE RESENT?',
      answer: 'Please visit our registration confirmation page and enter the email you registered with to check if you are preregistered. If you do not receive a confirmation email, please contact us at regsupport@magfest.org.',
    },
    {
      question: 'I CAN ONLY PURCHASE THE INITIAL BADGE AT THIS TIME. WILL I BE ABLE TO ADD A KICK-IN LEVEL AT A LATER DATE?',
      answer: 'Sure! If you look at your registration confirmation email you will find a personalized link that will allow you to edit your details and make any kick-in purchases. Please note: you will have to pay for the kick-in level when you select it.',
    },
    {
      question: 'I APPLIED FOR VENDOR SPACE IN THE MAGFEST MARKETPLACE. SHOULD I PURCHASE A BADGE JUST IN CASE MY APPLICATION IS NOT APPROVED?',
      answer: 'While there is no prohibition on purchasing a MAGFest badge while your application is being reviewed or you are on the waitlist, it is in your best interest to wait until you hear back. This will assist us greatly in setting up our vendor space and ensuring that all your badges are in the same group. We don\'t expect to sell out on badges and the badge price will not be increasing in the preregistration stage.',
    },
    {
      question: 'I AM NO LONGER ABLE TO ATTEND MAGLABS. CAN I GET A REFUND?',
      answer: 'No. MAGFest has a no-refund policy for all registrations. If for any reason you can\'t make it, we allow and encourage you to resell your registration for no more than the exact price you paid for it.'
    },
    {
      question: 'HOW MUCH ARE BADGES FOR CHILDREN? DO THEY NEED TO BE REGISTERED?',
      answer: 'Each attendee, including children, will need to be registered and have a badge. All children 6 through 12 get a half-price discount off the badge price. Children 5 and under are free.'
    },
    {
      question: 'DO I HAVE TO STAY WITH MY CHILD?',
      answer:'<p>All attendees under 18 will need to provide a signed parental consent form upon picking up their badge, which must be notarized if they are not accompanied by their legal guardian. If one was not completed prior to the badge being picked up, the guardian must sign the parental consent form at Registration.</p><p>All children 12 and under will need to be accompanied by an adult with a paid badge and wear the corresponding wristband. Children having their 13th birthday during the event may upgrade their badge so they no longer need to be accompanied but will need to pay the difference between the discounted badge and current badge price.</p>'
    },
    {
      question: 'DOES MAGLABS OFFER A GROUP DISCOUNT?',
      answer: 'Yes! During pre-registration, groups of 8 or more can buy badges at a $5 discount off the badge price. A group leader purchases the group registration, and after payment, the leader will receive a group management link, which can be used to fill in the information about the group\'s members.'
    },
    {
      question: 'I PURCHASED MY BADGE THROUGH A GROUP. CAN I PICK UP MY OWN BADGE?',
      answer: 'Please ensure that your group leader has assigned all the badges for their group prior to coming to the event. If they have assigned you a badge then you can pick it up like a normal attendee.'
    },
    {
      question: 'MY GROUP LEADER HAS NOT ASSIGNED OUR BADGES. HOW DO I PICK UP MY BADGE?',
      answer: 'Your group leader must be present to confirm that you can claim one of the badges in the group. If your badge has not been assigned and your group leader is not with you when you attempt to pick up your badge, you will be instructed to return with your group leader.'
    },
    {
      question: 'HOW DO I ADD MORE BADGES TO MY GROUP?',
      answer: 'In your MAGLabs group payment received email there is a link to your group management page. You can find a button at the bottom of that page to add more badges.',
      note: 'Please note, you can only add five or more badges and you will be asked to make payment for the extra badges at that time.'
    },
    {
      question: 'HOW DO I ADD A MINOR TO MY GROUP? WHAT DISCOUNTS DO THEY GET?',
      answer: '<p>Badges for minors cost 50% off the full badge price. They do not get an additional group discount, and must be added to a group by a Registration staffer. Minors five and under are free.</p><p>If you would like to add a minor to your group just send an email to regsupport@magfest.org with the details. If you have already purchased a group badge for a minor we can refund the discount difference. Please make sure to include the minor\'s birthday in your email so we can give them the appropriate discount.</p>'
    },
    {
      question: 'WILL MY BADGES AND KICK-IN ITEMS BE MAILED TO ME PRIOR TO THE EVENT?',
      answer: 'Badges and kick-in items are not mailed out before the event. Your badge will be available for pickup at the Registration desk when you arrive at MAGLabs and your kick-in items will be available for pickup at the Merchandise area.'
    },
    {
      question: 'I REQUIRE SPECIAL ASSISTANCE / HAVE A MEDICAL REASON THAT PREVENTS ME FROM WAITING IN LINE FOR MY BADGE. WILL THIS BE ACCOMMODATED?',
      answer: 'Yes! Just let one of the line wranglers or security people know and they will escort you to the VIP line.'
    },
    {
      question: 'I BOUGHT MORE THAN ONE BADGE IN MY NAME. WILL THIS PRESENT A PROBLEM WHEN PICKING UP MY BADGES?',
      answer: 'Yes. MAGFest has a one badge per person policy so you will only be able to pick up one badge for yourself. If you are buying a badge for another individual, we ask that you put that individual\'s information into the registration form. This will allow for a faster pickup process in the preregistration line, as otherwise we will have to reassign your extra badges before they can be handed out. You may also use the personalized link in your MAGLabs payment received email to change the name on the badge.',
      note: 'If you are buying the badge as a surprise, we still ask that you use the individual\'s information when purchasing the badge, but make sure to use your email address so they don\'t get the confirmation email.'
    },
    {
      question: 'WHAT DO I NEED TO BRING TO PICK UP MY BADGE?',
      answer: 'Anyone picking up a badge needs a government issued photo ID that matches the name of the badge being picked up and your date of birth. Please ensure that you use your legal name as shown on your ID when you preregister for your badge. If you used another name, email regsupport@magfest.org or use the personalized link in your confirmation email to transfer your badge to your corrected name.',
      note: 'On rare occasions we will accept a photo ID without a date of birth such as a high school or college ID. Please note, we do reserve the right to refuse these IDs and anyone using a high school photo ID will also need to bring a signed parental consent form, which must be notarized if they are not accompanied by a legal guardian regardless of age.'
    },
    {
      question: 'WHAT IF I DO NOT HAVE A PHOTO ID? CAN I STILL PICK UP MY BADGE?',
      answer: 'We understand that people under 18 often do not have an official photo ID, so a signed parental consent form, which must be notarized if they are not accompanied by a legal guardian, will suffice for minors. For all other cases, please notify us ahead of time at regsupport@magfest.org to make arrangements – this makes it much easier for us to accommodate you. If you do not make arrangements with us beforehand and do not have a photo ID, we will do our best but cannot guarantee that you will be able to pick up your badge.'
    },
    {
      question: 'CAN I PICK UP A BADGE FOR ANOTHER INDIVIDUAL?',
      answer: 'NO. Each badge must be picked up by the specific individual whose name the badge is under and they must have a government issued photo ID to claim it. You may not bring their photo ID to pick up the badge. Legal guardians may hold the badge for their child, but we ask that the child be present when the badge is received.'
    },
    {
      question: 'WILL THE LEGAL NAME THAT I USED WHEN PURCHASING MY REGISTRATION BE PRINTED ON MY BADGE?',
      answer: 'We understand that some would prefer their name not be printed on their badge. Not to fear, names are not printed on badges. When you receive your badge you\'ll have the opportunity to write whatever you\'d like on it.'
    },
    {
      question: 'I LOST MY BADGE. WHAT DO I DO?',
      answer: 'Unfortunately, you will need to buy a new badge at the current price. If you find your initial badge later, bring both to Registration and we will note that you need a refund for your second badge.',
      note: 'Please note, we will make every effort to process your refunds at the event, but please allow us two weeks after the event to process your refund. If you have not received your refund at that time please email regsupport@magfest.org with your details.'
    },
    {
      question: 'I PURCHASED A SUPPORTER PACKAGE, WHY AM I GETTING AN ATTENDEE BADGE?',
      answer: '<p>All individuals that purchase a supporter package will also be given an attendee badge. While supporters will still receive a personalized swag item, supporter badges no longer exist. This prevents issues where some Supporters were given two valid badges upon registration, which is against MAGFest policy.</p><p>All supporter swag can be picked up at our Merchandise booth after you pick up your badge.</p>'
    },
    {
      question: 'I NO LONGER NEED MY HOTEL RESERVATION, WHAT SHOULD I DO WITH IT?',
      answer: 'If your room is in a MAGLabs room block, please call the hotel to cancel your reservation. The sale of the right to a reservation is not permitted.'
    },
    {
      question: 'WHAT ARE MAGFEST MPOINTS? HOW CAN THEY BE USED?',
      answer: 'MPoints are MAGFest currency that work like real money at the fest. Attendees can earn them through participation in contests and tournaments or through other events. They come in denominations of 1, 5, 10, and 20 points. Attendees can use MPoints like cash at charity events, the Marketplace, the MAGFest Merchandise Booth, and Rock Island. (They cannot be used at Registration.) MPoints are not convertible to cash.',
      note: 'MPoints that were earned at MAGFest 2018 can be used at MAGLabs 2018.'
    },
    {
      question: 'WHERE CAN I FIND MAPS AND SCHEDULES?',
      answer: 'Use the Guidebook app or website to view all scheduled activities during the weekend, and also view event maps.'
    },
    {
      question: 'WHAT IS MAGLABS\'S CODE OF CONDUCT?',
      answer: 'MAGLabs\'s code of conduct can be found here.'
    },
    {
      question: 'CAN I VAPE/USE MY E-CIGARETTE IN THE HOTEL?',
      answer: 'No. Vaping and use of e-cigs inside is against hotel policy, and state law. We have heard every reason why this shouldn\'t be so, but we can\'t change the law. Setting off false fire alarms in the hotel jeopardizes our ability to come back to our venue. Don\'t do it.'
    }
  ]
}

export default {
  state
}