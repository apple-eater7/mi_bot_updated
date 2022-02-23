
## Generated Story 6450094606205935414
* greet
    - utter_greet
    - utter_bot_actions
* new_order
    - utter_has_user_decided
* affirm
    - user_info_form
    - form{"name": "user_info_form"}
    - slot{"requested_slot": "user_name"}
* form: user_info_inform
    - form: rewind
* form: user_info_inform{"user_name": "divya"}
    - slot{"user_name": "divya"}
    - form: user_info_form
    - slot{"user_name": "divya"}
    - slot{"requested_slot": "email_id"}
* form: user_info_inform{"email_id": "divya.nallamalli@gmail.com"}
    - slot{"email_id": "divya.nallamalli@gmail.com"}
    - form: user_info_form
    - slot{"email_id": "divya.nallamalli@gmail.com"}
    - slot{"requested_slot": "devices_list"}
* form: user_info_inform{"devices_list": "xiaomi redmi 7a"}
    - slot{"devices_list": "xiaomi redmi 7a"}
    - form: user_info_form
    - slot{"devices_list": "xiaomi redmi 7a"}
    - form{"name": null}
    - slot{"requested_slot": null}
