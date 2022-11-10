/**
 * jspsych-html-keyboard-response
 * Josh de Leeuw
 *
 * plugin for displaying a stimulus and getting a keyboard response
 *
 * documentation: docs.jspsych.org
 *
 **/


jsPsych.plugins["html-keyboard-response-ld"] = (function() {

  var plugin = {};

  plugin.info = {
    name: 'html-keyboard-response-ld',
    description: '',
    parameters: {
      stimulus: {
        type: jsPsych.plugins.parameterType.HTML_STRING,
        pretty_name: 'Stimulus',
        default: undefined,
        description: 'The HTML string to be displayed'
      },
      choices: {
        type: jsPsych.plugins.parameterType.KEYCODE,
        array: true,
        pretty_name: 'Choices',
        default: jsPsych.ALL_KEYS,
        description: 'The keys the subject is allowed to press to respond to the stimulus.'
      },
        correct_choice:{
            type: jsPsych.plugins.parameterType.STRING,
            pretty_name: 'Correct choice',
            default: undefined,
            array:false,
            description: 'Label for the correct button.'
        },
        correct_text: {
          type: jsPsych.plugins.parameterType.STRING,
          pretty_name: 'Correct text',
          default: "<p class='feedback'>Correct</p>",
          description: 'String to show when Correct answer is given.'
        },
    incorrect_text: {
      type: jsPsych.plugins.parameterType.STRING,
      pretty_name: 'Incorrect text',
      default: "<p class='feedback'>Incorrect</p>",
      description: 'String to show when incorrect answer is given.'
    },
    toolong_text: {
    type: jsPsych.plugins.parameterType.STRING,
    pretty_name: 'Too long text',
    default: "<p class='feedback'>Incorrect</p>",
    description: 'String to show when time taken is too long.'
  },
      prompt: {
        type: jsPsych.plugins.parameterType.STRING,
        pretty_name: 'Prompt',
        default: null,
        description: 'Any content here will be displayed below the stimulus.'
      },
      stimulus_duration: {
        type: jsPsych.plugins.parameterType.INT,
        pretty_name: 'Stimulus duration',
        default: null,
        description: 'How long to hide the stimulus.'
      },
      trial_duration: {
        type: jsPsych.plugins.parameterType.INT,
        pretty_name: 'Trial duration',
        default: null,
        description: 'How long to show trial before it ends.'
      },
      response_ends_trial: {
        type: jsPsych.plugins.parameterType.BOOL,
        pretty_name: 'Response ends trial',
        default: true,
        description: 'If true, trial will end when subject makes a response.'
      },

    }
  }

  plugin.trial = function(display_element, trial) {

    var new_html = '<div id="jspsych-html-keyboard-response-stimulus">'+trial.stimulus+'</div>';

    // add prompt
    if(trial.prompt !== null){
      new_html += trial.prompt;
    }

    // draw
    display_element.innerHTML = new_html;

    // store response
    var response = {
      rt: null,
      key: null
    };

    // function to end trial when it is time
    var end_trial = function() {

      // kill any remaining setTimeout handlers
      jsPsych.pluginAPI.clearAllTimeouts();

      // kill keyboard listeners
      if (typeof keyboardListener !== 'undefined') {
        jsPsych.pluginAPI.cancelKeyboardResponse(keyboardListener);
      }
      var isCorrect = String.fromCharCode(response.key)==trial.correct_choice ;

      // gather the data to store for the trial

      var trial_data = {
        "rt": response.rt,
        "stimulus": trial.stimulus,
        "correct_answer": trial.correct_choice,
        "key_press": String.fromCharCode(response.key),
        "isCorrect" : isCorrect
      };

      // clear the display
      display_element.innerHTML = '';

      // move on to the next trial
      jsPsych.finishTrial(trial_data);
    };

      var end_trial_2 = function() {

        // kill any remaining setTimeout handlers
        jsPsych.pluginAPI.clearAllTimeouts();

        // kill keyboard listeners
        if (typeof keyboardListener !== 'undefined') {
          jsPsych.pluginAPI.cancelKeyboardResponse(keyboardListener);
        }
        display_element.innerHTML = trial.toolong_text;
        var keyboardListener = jsPsych.pluginAPI.getKeyboardResponse({
              callback_function: end_trial,
              valid_responses: ['enter'],
              rt_method: 'date',
              persist: false,
              allow_held_key: false
          });

      };

    // function to handle responses by the subject
    var after_response = function(info) {
        if (typeof keyboardListener !== 'undefined') {
          jsPsych.pluginAPI.cancelKeyboardResponse(keyboardListener);
        }
      // after a valid response, the stimulus will have the CSS class 'responded'
      // which can be used to provide visual feedback that a response was recorded
      display_element.querySelector('#jspsych-html-keyboard-response-stimulus').className += ' responded';

      // only record the first response
      if (response.key == null) {
        response = info;
      }
      /// wrong answer
      if(String.fromCharCode(response.key)!=trial.correct_choice){
        jsPsych.pluginAPI.clearAllTimeouts();
        display_element.innerHTML = trial.incorrect_text;
        var keyboardListener = jsPsych.pluginAPI.getKeyboardResponse({
            callback_function: end_trial,
          valid_responses: ['enter'],
            rt_method: 'date',
            persist: false,
            allow_held_key: false
        }
      );

      }
      else{
        if (trial.response_ends_trial) {
          jsPsych.pluginAPI.clearAllTimeouts();
          display_element.innerHTML = trial.correct_text;
          var keyboardListener = jsPsych.pluginAPI.getKeyboardResponse({
              callback_function: end_trial,
            valid_responses: ['enter'],
              rt_method: 'date',
              persist: false,
              allow_held_key: false
            }
          );
        }
      }

    };

    // start the response listener
    if (trial.choices != jsPsych.NO_KEYS) {
      var keyboardListener = jsPsych.pluginAPI.getKeyboardResponse({
        callback_function: after_response,
        valid_responses: trial.choices,
        rt_method: 'date',
        persist: false,
        allow_held_key: false
      });
    }

    // hide stimulus if stimulus_duration is set
    if (trial.stimulus_duration !== null) {
      jsPsych.pluginAPI.setTimeout(function() {
        display_element.querySelector('#jspsych-html-keyboard-response-stimulus').style.visibility = 'hidden';
      }, trial.stimulus_duration);
    }

    // end trial if trial_duration is set
    if (trial.trial_duration !== null) {
      jsPsych.pluginAPI.setTimeout(function() {
        end_trial_2();
      }, trial.trial_duration);
    }

  };

  return plugin;
})();
