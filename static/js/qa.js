phrase = document.getElementById('phraseText');
context = document.getElementById('contextText');
submit = document.getElementById('sideSubmit');

submit.onclick = function()  {
    if(((phrase.value).length) > 0) {
        if(((context.value).length) > 0) {
            answer_func((phrase.value, context.value))
        }
    }
    else {
        alert("You can't submit without Entering Text")
    }
}

function answer_func(phrase, context) {
    let xhr = new XMLHttpRequest();

    console.log('inside answer_func')
    xhr.open("POST", "/sideAnswer", true);
    //Send the proper header information along with the request
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onload = function () {
            console.log('inside answer_func Load')
            if (this.status == 200) {
                    // console.log(this.responseText)
                    outputAnswer = this.responseText
                    outputAnswer = JSON.parse(outputAnswer)
                    console.log(outputAnswer)

                    document.getElementById('sideAns').value = outputAnswer
            }
            else {
                    console.log("inside answer_func else")
            }
    }
    params = { "phrase": phrase, "context": context }
    xhr.send(JSON.stringify(params));
}