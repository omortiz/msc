// /static/custom.js
const quest_url = "http://127.0.0.1:5000/quest"

function submit_message(message) {
    $.post(quest_url, 
        {
        message: message
        }, 
        handle_response);

    function handle_response(data) {
        json_data =JSON.parse(data);
        console.log(typeof json_data)
        // append the bot repsonse to the div
        $('.chat-container').append(`
            <div class="row">
                <div class="chat-message col-md-5 offset-md-7 bot-message">`+
                    json_data.reply+
                `</div>
            </div>
          `);
        // remove the loading indicator
        $("#loading").remove();
    }
}
// /static/custom.js

$('#target').on('submit', function (e) {
    e.preventDefault();
    const input_message = $('#input_message').val()
    // return if the user does not enter any text
    if (!input_message) {
        return
    }

    $('.chat-container').append(`
        <div class="row">
            <div class="chat-message col-md-5 human-message">
                ${input_message}
            </div>
        </div>
        `)

    // loading 
    $('.chat-container').append(`
        <div class="row">
            <div class="chat-message text-center col-md-2 offset-md-10 bot-message" id="loading">
                <b>...</b>
            </div>
        </div>
        `)

    // clear the text input 
    $('#input_message').val('')

    // send the message
    submit_message(input_message)
});