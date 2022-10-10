async def sender(client, users, message, counter, what_to_hide):
    user = users[counter]

    try:
        message = await client.send_message(user, message, parse_mode='md')
        message_id = message.id
        recipient_id = int(message.peer_id.stringify().split('=')[1].replace(')', ''))
    
        try:
            user = await client.get_entity(recipient_id)
        except:
            print('Something went wrong. Can\'t get user')

        current_dialog = None

        async for dialog in client.iter_dialogs():
            if dialog.name == user.first_name:
                current_dialog = dialog

        if what_to_hide == 'message':
            await client.delete_messages(current_dialog, message_id, revoke=False)
        elif what_to_hide == 'chat':
            await client.delete_dialog(current_dialog, revoke=False)
        else:
            print('Wrong removing mode. Use «message» or «chat»')
    except:
        print('Something went wrong. Can\'t send message')