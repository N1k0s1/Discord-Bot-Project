Discord Server: https://discord.gg/pbNCukHC	
Features currently not working:	
Most of them, a few working, most require further debugging and lots of rewriting.	


### This bot is proof of concept, requirements/specification sheet listed below self-host instructions.

## Self Host Instructions

#### Prerequisites
1. **Python**: Ensure you have Python 3.8 or higher installed. You can download it from [python.org](https://www.python.org/downloads/).
2. **Discord Bot Token**: You need a bot token from the Discord Developer Portal. Create a new application and bot if you haven't already.

1. **Clone or Download the Repository**:
   - Clone your repository or download the code to your local machine.

2. **Install Required Libraries**:
   - Open a terminal or command prompt.
   - Navigate to the directory where your `main.py`file is located.
   - Install the required libraries using `pip`:
     ```sh
     pip install -r requirements.txt
     ```

3. **Set Up Your Bot Token**:
   - Add your bot token to the `.env` file:
     ```
     DISCORD_BOT_TOKEN=YOUR_BOT_TOKEN_HERE
     ```

4. **Run The Bot**:
   - In the terminal or command prompt, run the bot:
     ```sh
     python main.py
     ```

5. **Invite Your Bot to Your Server**:
   - Go to the Discord Developer Portal.
   - Navigate to your application and click on the "OAuth2" tab.
   - Under "OAuth2 URL Generator", select the `bot`scope and the necessary permissions for the bot.
   - Copy the generated URL and open it in your browser to invite the bot to your server.

6. **Verify The Bot is Running**:
   - Check the terminal for the message "We have logged in as [The Bot's Name]".
   - In your Discord server, use the `/ping` command to verify that the bot is responding.


1. User Validation and Credential Assignment


	•	Functionality: Validate new users upon joining the server.

	•	Prompt new users to enter their City, Program, and Cohort details.

	•	Assign roles based on the provided credentials.

	![image](https://github.com/user-attachments/assets/c6fe9885-716b-4cf8-a51e-cc937b69ce64)
	#### Cohort Management working. Cohort role assignment working, will work on City/Program/Cohort 


2. Cohort Management


	•	Functionality: Assign roles and create cohort-specific channels.

	•	Automatically assign a role to users based on their cohort.

	•	Create private text and audio channels for each cohort.

	•	Ensure each cohort’s channels are only accessible to members of that cohort and relevant staff.

3. Support Ticket Integration


	•	Functionality: Integrate a support ticket system.

	•	Allow users to create support tickets for various needs, including Well-being Coaching, Bug Reporting, and Tutor Support.

	•	Automatically assign tickets to the relevant support team members based on the ticket type.

	•	Provide a channel for tracking and updating the status of support tickets.

	•	Notify users when their ticket status changes or when further information is required.



4. Weekly Check-ins


	•	Functionality: Prompt learning spaces with check-ins & polls

	•	Schedule messages for the start and end of the week.

	•	Customize messages to encourage engagement and reflection on the week’s activities.



5. Nudges for Learners


	•	Functionality: Nudge learners for various reminders.

	•	Send reminders for overdue work.

	•	Acknowledge when work is completed with congratulatory messages.

	•	Gamify work completion by assigning level scores and tracking progress.

	•	Acknowledge birthdays with celebratory messages.

	•	Announce upcoming events and important announcements.



6. Automated Messaging


	•	Functionality: Schedule automated messages.

	•	Set up a schedule for automated messages to be sent at specified times & dates including a brief history of why it is a public holiday or time of historical context.

	•	Include reminders, motivational quotes, and other relevant content.



7. Suggestion Box


	•	Functionality: Create an automatic suggestion box.

	•	Allow users to submit suggestions anonymously.

	•	Compile suggestions and present them to administrators regularly.



8. Feedback Collection


	•	Functionality: Collect feedback from learners.

	•	Provide a platform for learners to give feedback on coaching and program experience.

	•	Ensure feedback can be submitted anonymously if desired.

	•	Compile feedback and present it to relevant staff for review.



9. Coaching Session Check-In 


	•	Functionality: Allow learners to “Check In” before a coaching session.

	•	Provide a prompt for learners to check in before their scheduled coaching session.

	•	Collect check-in data to help coaches prepare for the session.

	•	Ensure check-in information is easily accessible to coaches prior to the session.



Technical Requirements


Bot Hosting and Management


	•	Environment: Ensure the bot is hosted on a reliable server with 24/7 uptime.

	•	Maintenance: Regular updates and maintenance checks to ensure the bot runs smoothly.



Security and Privacy


	•	Data Protection: Ensure all user data collected is securely stored and handled according to privacy laws.

	•	Access Control: Only authorised staff should have access to sensitive data and bot management features.



Integration with Discord API


	•	API Usage: Leverage Discord’s API for user validation, role assignments, channel creation, and messaging.

	•	Rate Limits: Adhere to Discord’s rate limits to avoid bot disruptions.



Development Timeline


	1.	Week 1-2: Requirement gathering and finalising the specification.

	2.	Week 3-4: Initial development of user validation, credential assignment, and cohort management features.

	3.	Week 5-6: Development of weekly check-ins and nudges for learners.

	4.	Week 7-8: Implementation of automated messaging and suggestion box.

	5.	Week 9-10: Feedback collection and coaching session check-in feature development.

	6.	Week 11-12: Testing, bug fixing, and final adjustments.



Expected Deliverables


	1.	Fully functional Discord bot meeting all specified requirements.

	2.	Comprehensive documentation for bot usage and management.

	3.	Training session for staff on bot functionalities and maintenance.
