from __future__ import print_function
import random


def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" + event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])


def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()



def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    reprompt_text = "Just Starting"

    if reprompt_text == None:
        return listenGuessing(intent, session)
    elif intent_name == "StartGame":
        return get_welcome_reponse()
    elif intent_name == "Begin":
        return drawGame(intent, session)
    elif intent_name == "GuessPicture":
        return listenGuessing(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Functions that control the skill's behavior ------------------


def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    
    speech_output = "Welcome to the Alexa Pictionary Game. Please say draw to start game"

    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.

    reprompt_text = "Welcome to the Alexa Pictionary Game. Please say draw to start game"
    should_end_session = False
    card_title = reprompt_text
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def drawGame(intent, session):
    """ Randomly picks a picture to draw and sends instructions to draw it
    """
    
    
    session_attributes = {}
    should_end_session = False
    
    global LIST_OF_PICTURES
    LIST_OF_PICTURES = ['platypus', 'fork', 'amazon', 'cup', 'hand', 'batman', 'plant', 'dead pool', 'dolphin', 'apple'];
    
    global picNumber
    picNumber = random.randint(0,9)    
    
   
    speech_output = "Ready for guesses. Guess using it is"
    # if picNumber == 1:
    #     card_title = LIST_OF_PICTURES[picNumber]
    # elif picNumber == 2:
    #     card_title = LIST_OF_PICTURES[picNumber]
    # elif picNumber == 3:
    #     card_title = LIST_OF_PICTURES[picNumber]
    # elif picNumber == 4:
    #     card_title = LIST_OF_PICTURES[picNumber]
    # elif picNumber == 5:
    #     card_title = LIST_OF_PICTURES[picNumber]
    # elif picNumber == 6:
    #     card_title = LIST_OF_PICTURES[picNumber]
    # elif picNumber == 7:
    #     card_title = LIST_OF_PICTURES[picNumber]
    # elif picNumber == 8:
    #     card_title = LIST_OF_PICTURES[picNumber]
    # elif picNumber == 9:
    #     card_title = LIST_OF_PICTURES[picNumber]
    # elif picNumber == 10:
    #     card_title = LIST_OF_PICTURES[picNumber]
        
    reprompt_text = None
    card_title = "Attampting to draw: " + LIST_OF_PICTURES[picNumber]

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def listenGuessing(intent, session):

    should_end_session = False
    

    PictureAttempt = intent['slots']['PictureAttempt']['value']

    if  PictureAttempt not in LIST_OF_PICTURES:
        speech_output = "Not an option. Try Again "
        session_attributes = {}
        reprompt_text = "Keep trying " 
        
        
    elif LIST_OF_PICTURES[picNumber]== str(PictureAttempt):
        speech_output = "Correct. " + "The answer is " + str(PictureAttempt)
        should_end_session = True
        session_attributes = {}
        reprompt_text = "Good Job " 
        
    else:
        speech_output = "Nope. Try Again "
        session_attributes = {}
        reprompt_text = "Keep Going" 

    card_title = str(reprompt_text)
       
    return build_response(session_attributes, build_speechlet_response(
    card_title, speech_output, reprompt_text, should_end_session))


    # Setting reprompt_text to None signifies that we do not want to reprompt
    # the user. If the user does not respond or says something that is not
    # understood, the session will end.

# --------------- Helpers that build all of the responses ----------------------


def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': 'SessionSpeechlet - ' + title,
            'content': 'SessionSpeechlet - ' + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }