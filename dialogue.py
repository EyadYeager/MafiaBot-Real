from main import player

intro = ("🌙 Welcome to the mysterious town of MafiaVille! 🌟"

         " Congratulations, brave townsfolk! You find yourselves in "
         "the heart of a thrilling game of Mafia, where secrets, deception, and strategy will shape the fate of the "
         "town."
         "🔍 Quick Overview:"

         "- The town is divided into two factions: the Innocents and the Mafia."
         "- The Innocents aim to identify and eliminate the Mafia members, while the Mafia seeks to outnumber and "
         "control the town.)"
         "- Each player is assigned a role with unique abilities, including roles like citizen and roles with "
         "extra abilities like the doctor and the elusive Mafia members."

         "- As an Innocent, work together to identify and vote out Mafia members during the day."

         "🌟 Your Mission:"

         "- If you're part of the Mafia, be cunning and discreet as you plot with your fellow members to "
         "eliminate the townsfolk."
         "🌞 Day Phase:"

         "- Discuss openly in the town square, share suspicions, and vote to eliminate a player you believe is "
         "Mafia."
         "- Use your role's abilities wisely to gather information or protect others."
         "🌙 Night Phase:"

         "- Secrets unfold as the town sleeps. The Mafia will choose their target, and special roles will "
         "carry out their nightly duties.")

Day_dialogue = ("🌞 Good morning, MafiaVille! 🌄"
                "The sun rises, and the townsfolk gather in the square. It's time for discussion and decisions. Share "
                "your thoughts, suspicions, and observations about last night's events.)"
                "🗳️ Daytime Actions:"

                "- Use your vote wisely. Nominate a player you believe is part of the Mafia."
                "- Special roles, now is your chance to reveal any information or use your abilities to help the town.")
Night_summary = ("🌄 The dawn breaks over MafiaVille, revealing the aftermath of the night's events. ☀️"
                 "📢 Town Announcement:"
                 "- As morning arrives, the town gathers to learn the outcomes of the night's actions."

                 "🔍 Night Summary:"

                 "1. 🌙 **Mafia's Deeds:**"
                 f"- The Mafia targeted {not player.alive}. The lifeless body of {not player.alive} is discovered. "
                 "The town mourns their loss."

                 "2. 🩹 **Doctor's Intervention:**"
                 f"- The Doctor protected {not player.alive}. Thanks to the Doctor's swift action, {not player.alive} "
                 "survived the night unharmed."

                 "3. 🔍 **Detective's Investigation:**"
                 f"- The Detective investigated {not player.alive}'s role. After careful scrutiny, it is revealed that {not player.alive}"
                 "is [Innocent/Mafia]."

                 "🌟 The townsfolk react to the revelations. The loss of a comrade, the relief of survival, "
                 "and the uncovering of hidden identities shape the town's emotions."

                 "🤔 Day Phase begins anew. Townsfolk, it's time to discuss, vote, and unravel the mysteries of "
                 "MafiaVille! What strategies will you employ in the wake of last night's revelations?")

Announcements = ("📢 Town Announcement:"
                 f"- The town has decided! {not player.alive} has been accused of Mafia ties and is now on trial!"
                 f"🚨 Attention, {not player.alive} Defend yourself against the accusations. Your fate rests in the "
                 f"hands of"
                 "the townsfolk."
                 f"🌟 After heated discussion, the town votes. Will {not player.alive} be exonerated, or is the town "
                 f"one step"
                 "closer to uncovering the Mafia?")

Night_dialogue = ("🌙 As the sun sets, darkness falls over MafiaVille. 🌠"

                  "It's time for the Night Phase. Special roles, use your abilities wisely, but keep your actions a "
                  "secret.)"

                  "🌌 Nighttime Actions:"
                  "- Mafia members, choose your target carefully. The fate of the town depends on it."
                  "- Doctors, decide who to protect."
                  "- Detectives, select a player to investigate."

                  "🤫 The town sleeps, unaware of the secret dealings happening in the shadows. Await the morning "
                  "light to reveal the outcomes of your decisions.")


game_end_Mafia = ("🌟 The shadows lengthen in MafiaVille as the Mafia emerges triumphant! 🎭"
                  "🔍 Town Announcement:"

                  "- In a stunning turn of events, the Mafia has outsmarted the townsfolk! The streets belong to the "
                  "[Mafia]!"

                  "😈 The Mafia members celebrate their successful infiltration and control of the town. Their "
                  "devious schemes have left the townsfolk powerless."
                  "🌆 Mafia Victory Speech:"

                  "- Congratulations to the cunning Mafia members who orchestrated this brilliant victory. Your "
                  "strategies and covert actions have shaped the fate of MafiaVille."
                  "🎭 Reflect on the alliances formed, the betrayals executed, and the covert operations that led "
                  "to this moment. Until the next game, the town remains under the watchful eyes of the victorious "
                  "Mafia."
                  "🌙 Thank you for playing in this thrilling round of MafiaVille! 🌟")

game_end_Town = ("🌟 Light breaks through the darkness as the townsfolk of MafiaVille emerge triumphant! 🌅"
                 "🔍 Town Announcement:)"

                 "- Against all odds, the townsfolk have prevailed! The [Innocents] are the true heroes of MafiaVille!"
                 "🎉 The town square erupts in cheers and celebrations as the Innocents successfully rooted out the "
                 "Mafia members, ensuring the safety of MafiaVille."


                 "🎊 Town Victory Speech:"

                 "- A heartfelt congratulations to the brave townsfolk who stood united against the Mafia threat. "
                 "Your vigilance, strategy, and collective efforts have secured victory for the town."
                 "🌅 Reflect on the alliances forged, the strategies employed, and the sacrifices made to protect "
                 "MafiaVille. As the sun rises on a peaceful town, the townsfolk can rest assured that justice has "
                 "prevailed."

                 "🌟 Thank you for playing in this triumphant round of MafiaVille! 🎊")
