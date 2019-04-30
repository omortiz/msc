// /static/custom.js
const quest_url = "http://127.0.0.1:5000/quest"

function submit_message(message) {
    $.post(quest_url, {
            message: message
        },
        handle_response);

    function handle_response(data) {
        const json_data = JSON.parse(data);

        // remove the loading indicator
        $("#loading").remove();
        
        // append the bot repsonse to the div
        $('#window').append(`
            <div class = "chat friend">
                <div class = "user-photo"><img src= "./assest/bot.png"></div>
                <p class = "chat-message">${json_data.reply}</p>
            </div>
          `);

    }
}
// /static/custom.js

$('#clickable').click(function (e) {
    e.preventDefault();
    const input_message = $('#question').val();
    // return if the user does not enter any text
    if (!input_message) {
        return
    }

    $('#window').append(`
        <div class = "chat self">
            <div class = "user-photo"><img src ="./assest/client.png"></div>
            <p class = "chat-message">${input_message}</p>
        </div>
        `)

    // loading 
    $('#window').append(`
        <div class = "chat friend" id="loading">
            <div class = "user-photo"><img src= "./assest/bot.png"></div>
            <p class = "chat-message">......</p>
        </div>
        `)

    // clear the text input 
    $('#question').val('')

    // send the message
    submit_message(input_message)
});