from .base import BaseAPI


class CallFireAPIVersion2(BaseAPI):
    """CallFire API v2 wrapper.

    Auto-generated based on https://www.callfire.com/v2/api-docs/swagger.json
    """
    #: Base API url
    BASE_URL = '1https://api.callfire.com/v2'

    def find_calls(self, query=None):
        """Find calls.

        Finds all calls sent or received by the user. Use "id=0" for the
        campaignId parameter to query for all calls sent through the POST
        /calls API. See [call states and
        results](https://developers.callfire.com/results-responses-errors.html)

        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        :query integer limit: Maximum number of records to return in a paged
        list response. The default is 100.
        :query integer offset: Offset to the start of a given page. The default
        is 0.
        :query array id: Comma seperated list of call ids to query for.
        :query integer campaignId: Query for calls inside of a particular
        campaign.
        :query integer batchId: ~
        :query string fromNumber: E.164 number that calls are from
        :query string toNumber: E.164 number that calls are to
        :query string label: Label for a specific call
        :query string states: Expected call statuses in comma seperated string
        (READY, SELECTED, CALLBACK, FINISHED, DISABLED, DNC, DUP, INVALID,
        TIMEOUT, PERIOD_LIMIT)
        :query string results: Expected call results in comma seperated string
        (SENT, RECEIVED, DNT, TOO_BIG, INTERNAL_ERROR, CARRIER_ERROR,
        CARRIER_TEMP_ERROR, UNDIALED)
        :query boolean inbound: Is the call inbound, false for outbound
        :query integer intervalBegin: Start of the find interval in Unix time
        milliseconds
        :query integer intervalEnd: End of the find interval in Unix time
        milliseconds
        """
        return self._get('/calls', query=query)

    def send_calls(self, query=None, body=None):
        """Send calls.

        Use the /calls API to quickly send individual calls. A verified Caller
        ID and sufficient credits are required to make a call.

        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        :query integer campaignId: Specify a campaignId to send calls quickly
        on a previously created campaign
        :query string defaultLiveMessage: ~
        :query string defaultMachineMessage: ~
        :query integer defaultLiveMessageSoundId: ~
        :query integer defaultMachineMessageSoundId: ~
        :query string defaultVoice: ~
        :body body: Array of CallRecipient objects
        :body -> CallRecipient string liveMessage: ~
        :body -> CallRecipient string transferDigit: ~
        :body -> CallRecipient string dialplanXml: ~
        :body -> CallRecipient integer liveMessageSoundId: ~
        :body -> CallRecipient string transferMessage: ~
        :body -> CallRecipient integer contactId: ~
        :body -> CallRecipient string phoneNumber: ~
        :body -> CallRecipient integer machineMessageSoundId: ~
        :body -> CallRecipient string machineMessage: ~
        :body -> CallRecipient object attributes: ~
        :body -> CallRecipient integer transferMessageSoundId: ~
        :body -> CallRecipient string voice: ~
        :body -> CallRecipient string transferNumber: ~
        """
        return self._post('/calls', query=query, body=body)

    def find_call_broadcasts(self, query=None):
        """Find call broadcasts.

        Find all voice broadcasts created by the user. Can query on label,
        name, and the current running status of the campaign. Returns a paged
        list of voice broadcasts.

        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        :query integer limit: Maximum number of records to return in a paged
        list response. The default is 100.
        :query integer offset: Offset to the start of a given page. The default
        is 0.
        :query string label: Label of voice broadcast
        :query string name: Name of voice broadcast
        :query boolean running: Specify if the campaigns should be running or
        not
        """
        return self._get('/calls/broadcasts', query=query)

    def create_call_broadcast(self, query=None, body=None):
        """Create a call broadcast.

        Create a voice broadcast campaign using the Voice Broadcast API. Send a
        CallBroadcast in the message body to detail a voice broadcast campaign.
        A campaign can be created with no contacts and bare minimum
        configuration, but contacts will have to be added further on to use the
        campaign.

        :query boolean start: Specify whether to immediately start this
        campaign (not required)
        :body body: callBroadcast
        :body -> CallBroadcast string status: Status of broadcast *read only*
        :body -> CallBroadcast string fromNumber: E.164 number
        :body -> CallBroadcast string name: Name of broadcast
        :body -> CallBroadcast array recipients: Recipients of broadcast
        :body -> CallBroadcast integer lastModified: DateTime formatted in unix
        time *read only*
        :body -> CallBroadcast array labels: Labels of broadcast
        :body -> CallBroadcast string dialplanXml: ~
        :body -> CallBroadcast integer maxActive: Max number of active calls
        :body -> CallBroadcast boolean resumeNextDay: ~
        :body -> CallBroadcast array schedules: ~
        :body -> CallBroadcast localTimeRestriction: LocalTimeRestriction
        object
        :body -> CallBroadcast string answeringMachineConfig:
        AnsweringMachineConfig object
        :body -> CallBroadcast sounds: ~
        :body -> CallBroadcast integer id: Id of broadcast
        :body -> CallBroadcast integer maxActiveTransfers: Max number of active
        transfers
        :body -> CallBroadcast retryConfig: RetryConfig object
        """
        return self._post('/calls/broadcasts', query=query, body=body)

    def get_call_broadcast(self, id, query=None):
        """Find a specific call broadcast.

        Returns a single CallBroadcast instance for a given call broadcast
        campaign id

        :path integer id: Id of CallBroadcast
        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        """
        return self._get('/calls/broadcasts/{id}'.format(id=id), query=query)

    def update_call_broadcast(self, id, body=None):
        """Update a call broadcast.

        After having created a voice broadcast campaign, this PUT lets the user
        modify the configuration of a voice broadcast campaign. See
        CallBroadcast for more information on what can/can't be updated on this
        API.

        :path integer id: The id of the voice broadcast
        :body body: callBroadcast
        :body -> CallBroadcast string status: Status of broadcast *read only*
        :body -> CallBroadcast string fromNumber: E.164 number
        :body -> CallBroadcast string name: Name of broadcast
        :body -> CallBroadcast array recipients: Recipients of broadcast
        :body -> CallBroadcast integer lastModified: DateTime formatted in unix
        time *read only*
        :body -> CallBroadcast array labels: Labels of broadcast
        :body -> CallBroadcast string dialplanXml: ~
        :body -> CallBroadcast integer maxActive: Max number of active calls
        :body -> CallBroadcast boolean resumeNextDay: ~
        :body -> CallBroadcast array schedules: ~
        :body -> CallBroadcast localTimeRestriction: LocalTimeRestriction
        object
        :body -> CallBroadcast string answeringMachineConfig:
        AnsweringMachineConfig object
        :body -> CallBroadcast sounds: ~
        :body -> CallBroadcast integer id: Id of broadcast
        :body -> CallBroadcast integer maxActiveTransfers: Max number of active
        transfers
        :body -> CallBroadcast retryConfig: RetryConfig object
        """
        return self._put('/calls/broadcasts/{id}'.format(id=id), body=body)

    def archive_voice_broadcast(self, id):
        """Archive voice broadcast.

        Archive a voice broadcast

        :path integer id: Id of voice broadcast to archive
        """
        return self._post('/calls/broadcasts/{id}/archive'.format(id=id))

    def get_call_broadcast_batches(self, id, query=None):
        """Find batches in a call broadcast.

        This endpoint will enable the user to page through all of the batches
        for a particular voice broadcast campaign.

        :path integer id: The id of the voice broadcast
        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        :query integer limit: Maximum number of records to return in a paged
        list response. The default is 100.
        :query integer offset: Offset to the start of a given page. The default
        is 0.
        """
        return self._get('/calls/broadcasts/{id}/batches'.format(id=id),
                         query=query)

    def add_call_broadcast_batch(self, id, body=None):
        """Add batches to a call broadcast.

        The add batch API allows the user to add additional batches to an
        already created voice broadcast campaign. The added batch will go
        through the CallFire validation process, unlike in the recipients
        version of this API. Because of this, use the scrubDuplicates flag to
        remove duplicates from your batch. Batches may be added as a contact
        list id, a list of contact ids, or a list of numbers.

        :path integer id: The id of the voice broadcast
        :body body: request
        :body -> BatchRequest boolean scrubDuplicates: Remove duplicate
        recipients in batch
        :body -> BatchRequest array recipients: List of Recipient objects
        :body -> BatchRequest string name: Name of batch
        :body -> BatchRequest integer contactListId: Id of contact list
        """
        return self._post('/calls/broadcasts/{id}/batches'.format(id=id),
                          body=body)

    def get_call_broadcast_calls(self, id, query=None):
        """Find calls in a call broadcast.

        This endpoint will enable the user to page through all of the calls for
        a particular voice broadcast campaign.

        :path integer id: The id of the voice broadcast
        :query integer batchId: ~
        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        :query integer limit: Maximum number of records to return in a paged
        list response. The default is 100.
        :query integer offset: Offset to the start of a given page. The default
        is 0.
        """
        return self._get('/calls/broadcasts/{id}/calls'.format(id=id),
                         query=query)

    def add_call_broadcast_recipients(self, id, query=None, body=None):
        """Add recipients to a call broadcast.

        Use this API to add recipients to an already created voice broadcast.
        Post a list of Recipient objects for them to be immediately added to
        the voice broadcast campaign. These contacts do not go through
        validation process, and will be acted upon as they are added.
        Recipients may be added as a list of contact ids, or list of numbers.

        :path integer id: The id of the voice broadcast to update
        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        :body body: recipients
        :body -> Recipient object attributes: Map of string attributes
        associated with recipient
        :body -> Recipient integer contactId: Id of contact for recipient
        :body -> Recipient string phoneNumber: E.164 number
        """
        return self._post('/calls/broadcasts/{id}/recipients'.format(id=id),
                          query=query, body=body)

    def start_voice_broadcast(self, id):
        """Start voice broadcast.

        Start a voice broadcast

        :path integer id: Id of voice broadcast to start
        """
        return self._post('/calls/broadcasts/{id}/start'.format(id=id))

    def get_call_broadcast_stats(self, id, query=None):
        """Get statistics on call broadcast.

        Returns statistics on CallBroadcast instance for given call broadcast
        campaign id

        :path integer id: ~
        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        :query integer begin: ~
        :query integer end: ~
        """
        return self._get('/calls/broadcasts/{id}/stats'.format(id=id),
                         query=query)

    def stop_voice_broadcast(self, id):
        """Stop voice broadcast.

        Stop a voice broadcast

        :path integer id: Id of voice broadcast to stop
        """
        return self._post('/calls/broadcasts/{id}/stop'.format(id=id))

    def get_call_recording(self, id, query=None):
        """Get call recording by id.

        Returns call recording

        :path integer id: ~
        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        """
        return self._get('/calls/recordings/{id}'.format(id=id), query=query)

    def get_call_recording_mp3(self, id):
        """Get call recording in mp3 format.

        Returns call recording

        :path integer id: ~
        """
        return self._get('/calls/recordings/{id}.mp3'.format(id=id))

    def get_call(self, id, query=None):
        """Find a specific call.

        Returns a single Call instance for a given call id.

        :path integer id: Id of call
        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        """
        return self._get('/calls/{id}'.format(id=id), query=query)

    def get_call_recordings(self, id, query=None):
        """Get call recordings for a call.

        Returns call recordings

        :path integer id: ~
        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        """
        return self._get('/calls/{id}/recordings'.format(id=id), query=query)

    def get_call_recording_by_name(self, id, name, query=None):
        """Get call recording by name.

        Returns call recording

        :path integer id: ~
        :path string name: ~
        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        """
        return self._get(
            '/calls/{id}/recordings/{name}'.format(id=id, name=name),
            query=query)

    def get_call_recording_mp3_by_name(self, id, name):
        """Get call mp3 recording by name.

        Returns call recording

        :path integer id: ~
        :path string name: ~
        """
        return self._get(
            '/calls/{id}/recordings/{name}.mp3'.format(id=id, name=name))

    def get_campaign_batch(self, id, query=None):
        """Find a specific batch.

        Returns a single Batch instance for a given batch id. This API is
        useful for determining the state of a validating batch.

        :path integer id: Id of batch
        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        """
        return self._get('/campaigns/batches/{id}'.format(id=id), query=query)

    def update_campaign_batch(self, id, body=None):
        """Update a batch.

        Update to a single Batch instance. May only change enabled at this
        time.

        :path integer id: Id of batch to update
        :body body: batch
        :body -> Batch string status: Status of batch (NEW, VALIDATING, ERRORS,
        SOURCE_ERROR, ACTIVE)
        :body -> Batch string name: Name of batch
        :body -> Batch integer created: DateTime formatted in unix time
        :body -> Batch integer broadcastId: Id of broadcast
        :body -> Batch boolean enabled: Is batch enabled
        :body -> Batch integer remaining: Number of contacts remaining
        :body -> Batch integer id: Id of batch
        :body -> Batch integer size: Size of batch
        """
        return self._put('/campaigns/batches/{id}'.format(id=id), body=body)

    def find_campaign_sounds(self, query=None):
        """Find sounds.

        Find all campaign sounds that were created by the user. These are all
        of the available sounds to be used in campaigns.

        :query integer limit: Maximum number of records to return in a paged
        list response. The default is 100.
        :query integer offset: Offset to the start of a given page. The default
        is 0.
        :query string filter: Name of file to search on
        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        """
        return self._get('/campaigns/sounds', query=query)

    def post_call_campaign_sound(self, query=None, body=None):
        """Add sound via call.

        Use this API to create a sound via phone call. Supply the required
        phone number in the CallCreateSound object inside of the request, and
        the user will receive a call shortly after with instructions on how to
        record a sound over the phone.

        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        :body body: callCreateSound
        :body -> CallCreateSound string toNumber: E.164 number to call to
        record sound
        :body -> CallCreateSound string name: Name of sound to create
        """
        return self._post('/campaigns/sounds/calls', query=query, body=body)

    def post_file_campaign_sound(self, query=None):
        """Add sound via file.

        Use this API to create a campaign sound file via a supplied .mp3 or
        .wav file.

        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        """
        return self._post('/campaigns/sounds/files', query=query)

    def post_campaign_sound(self, query=None, body=None):
        """Add sound via text-to-speech.

        Use this API to create a sound file via a supplied string of text. Send
        the required text in the TextToSpeech.message field, and pick a voice
        in the TextToSpeech.voice field. Available voices are: MALE1, FEMALE1 ,
        FEMALE2, SPANISH1, FRENCHCANADIAN1

        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        :body body: textToSpeech
        :body -> TextToSpeech string message: Text to be used to turn into
        sound
        :body -> TextToSpeech string voice: The voice to be used (MALE1,
        FEMALE1 , FEMALE2, SPANISH1, FRENCHCANADIAN1)
        """
        return self._post('/campaigns/sounds/tts', query=query, body=body)

    def get_campaign_sound(self, id, query=None):
        """Find a specific sound.

        Returns a single CampaignSound instance for a given campaign sound id.
        This is the meta data to the sounds only. No audio data is returned
        from this API.

        :path integer id: Id of CampaignSound
        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        """
        return self._get('/campaigns/sounds/{id}'.format(id=id), query=query)

    def get_campaign_sound_data_mp3(self, id):
        """Download a MP3 sound.

        Download the MP3 version of the hosted file. This is an audio data
        endpoint.

        :path integer id: Id of CampaignSound
        """
        return self._get('/campaigns/sounds/{id}.mp3'.format(id=id))

    def get_campaign_sound_data_wav(self, id):
        """Download a WAV sound.

        Download the WAV version of the hosted file. This is an audio data
        endpoint.

        :path integer id: Id of CampaignSound
        """
        return self._get('/campaigns/sounds/{id}.wav'.format(id=id))

    def find_contacts(self, query=None):
        """Find contacts.

        Find contacts by id, contact list, or on any property name. Returns a
        paged list of contacts.

        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        :query integer limit: Maximum number of records to return in a paged
        list response. The default is 100.
        :query integer offset: Offset to the start of a given page. The default
        is 0.
        :query array id: Multiple contact ids can be specified. If the id
        parameter is included, the other query parameters are ignored.
        :query array number: Multiple contact numbers can be specified. If the
        number parameter is included, the other query parameters are ignored.
        :query integer contactListId: A particular contact list to search by
        :query string propertyName: Name of contact property to search by
        :query string propertyValue: Value of contact property to search by
        """
        return self._get('/contacts', query=query)

    def create_contacts(self, body=None):
        """Create contacts.

        Create contacts in the CallFire system. These contacts are not
        validated on creation. They will be validated upon being added to a
        campaign.

        :body body: contacts
        :body -> Contact string workPhone: E.164 number
        :body -> Contact string mobilePhone: E.164 number
        :body -> Contact string firstName: First name of contact
        :body -> Contact boolean deleted: Return deleted contacts
        :body -> Contact string lastName: Last name of contact
        :body -> Contact string zipcode: ZIP code of contact
        :body -> Contact object properties: Map of string properties for
        contact
        :body -> Contact string externalId: External id of contact for syncing
        with external sources
        :body -> Contact string externalSystem: External system that external
        id refers to
        :body -> Contact integer id: Id of contact
        :body -> Contact string homePhone: E.164 number
        """
        return self._post('/contacts', body=body)

    def find_dnc_contacts(self, query=None):
        """Find DNCs.

        Find all Do Not Contact (DNC) objects created by the user. These
        DoNotContact entries only affect calls/texts/campaigns on this account.
        Returns a paged list of DoNotContact.

        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        :query integer limit: Maximum number of records to return in a paged
        list response. The default is 100.
        :query integer offset: Offset to the start of a given page. The default
        is 0.
        :query string prefix: Prefix (1-10 digits) of numbers
        :query integer dncListId: A DncList id to search for DNCs within
        :query string dncListName: A DncList name to search for DNCs within
        :query boolean callDnc: Is it a Call DNC
        :query boolean textDnc: Is it a Text DNC
        """
        return self._get('/contacts/dncs', query=query)

    def update_dnc_number(self, body=None):
        """Update a DNC.

        Update a Do Not Contact (DNC) contact value. Can toggle whether the DNC
        is enabled for calls/texts.

        :body body: doNotContact
        :body -> DoNotContact boolean text: Is number on DNT list
        :body -> DoNotContact boolean call: Is number on DNC list
        :body -> DoNotContact string number: E.164 number
        :body -> DoNotContact integer listId: Id of list
        """
        return self._put('/contacts/dncs', body=body)

    def find_contact_lists(self, query=None):
        """Find contact lists.

        Find all contact lists for the CallFire Developer. Returns a paged list
        of contact lists.

        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        :query integer limit: Maximum number of records to return in a paged
        list response. The default is 100.
        :query integer offset: Offset to the start of a given page. The default
        is 0.
        :query string name: Name or partial name of contact list
        """
        return self._get('/contacts/lists', query=query)

    def create_contact_list(self, body=None):
        """Create contact lists.

        Creates a contact list for use with campaigns using 1 of 3 inputs. A
        List of Contact objects, a list of String E.164 numbers, or a list of
        CallFire contactIds can be used as the data source for the created
        contact list. After staging these contacts into the CallFire system,
        contact lists go through seven system safeguards that check the
        accuracy and consistency of the data. For example, our system checks if
        a number is formatted correctly, is invalid, is duplicated in another
        contact list, or is on a specific DNC list. The default resolution in
        these safeguards will be to remove contacts that are against these
        rules. If contacts are not being added to a list, this means the data
        needs to be properly formatted and correct before calling this API.

        :body body: request
        :body -> CreateContactListRequest array contactIds: List of ids for
        contacts
        :body -> CreateContactListRequest array contactNumbers: List of E.164
        numbers
        :body -> CreateContactListRequest string contactNumbersField: Type of
        phone number (homePhone, workPhone, mobilePhone)
        :body -> CreateContactListRequest string name: Name of contact list
        :body -> CreateContactListRequest array contacts: List of Contact
        objects
        """
        return self._post('/contacts/lists', body=body)

    def create_contact_list_from_file(self):
        """Create contact list from file.

        Create a contact list for use with campaigns through uploading a .csv
        file

        """
        return self._post('/contacts/lists/upload')

    def delete_contact_list(self, id):
        """Delete a contact list.

        Deletes a contact list. The contacts inside are not deleted.

        :path integer id: Id of contact list to be deleted
        """
        return self._delete('/contacts/lists/{id}'.format(id=id))

    def get_contact_list(self, id, query=None):
        """Find a specific contact list.

        Returns a single ContactList instance for a given contact list id

        :path integer id: Id of contact list to return
        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        """
        return self._get('/contacts/lists/{id}'.format(id=id), query=query)

    def update_contact_list(self, id, body=None):
        """Update a contact list.

        Update contact list. Currently, only the contact list name is
        modifiable from this endpoint.

        :path integer id: Id of contact list to update
        :body body: request
        :body -> UpdateContactListRequest string name: Name of list
        """
        return self._put('/contacts/lists/{id}'.format(id=id), body=body)

    def remove_contact_list_items(self, id, query=None):
        """Delete contacts from a contact list.

        Delete contacts from a contact list. Multiple deletes in one request by
        repeating the "id" query parameter.

        :path integer id: Id of Contact entity inside the CallFire system.
        :query array contactId: ~
        """
        return self._delete('/contacts/lists/{id}/items'.format(id=id),
                            query=query)

    def get_contact_list_items(self, id, query=None):
        """Find contacts in a contact list.

        Find all entries in a given contact list. Returns a paged list of
        Contact entries.

        :path integer id: Id of contact list
        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        :query integer limit: Maximum number of records to return in a paged
        list response. The default is 100.
        :query integer offset: Offset to the start of a given page. The default
        is 0.
        """
        return self._get('/contacts/lists/{id}/items'.format(id=id),
                         query=query)

    def add_contact_list_items(self, id, body=None):
        """Add contacts to a contact list.

        Add contacts to a contact list by number, contact id, or Contact
        object.

        :path integer id: Id of contact list
        :body body: request
        :body -> AddContactListContactsRequest array contactIds: List of ids
        for contacts
        :body -> AddContactListContactsRequest array contactNumbers: List of
        E.164 numbers
        :body -> AddContactListContactsRequest string contactNumbersField: Type
        of phone number (homePhone, workPhone, mobilePhone)
        :body -> AddContactListContactsRequest array contacts: List of Contact
        object
        """
        return self._post('/contacts/lists/{id}/items'.format(id=id),
                          body=body)

    def remove_contact_list_item(self, id, contactId):
        """Delete a contact from a contact list.

        Delete a single contact from a contact list.

        :path integer id: ~
        :path integer contactId: Id of contact
        """
        return self._delete(
            '/contacts/lists/{id}/items/{contactId}'.format(id=id,
                                                            contactId=contactId))

    def delete_contact(self, id):
        """Delete a contact.

        Delete a contact. This doesn't actually delete the contact, it just
        removes the contact from any contact lists and marks the contact as
        deleted so won't show up when searching for contacts.

        :path integer id: Id of contact
        """
        return self._delete('/contacts/{id}'.format(id=id))

    def get_contact(self, id, query=None):
        """Find a specific contact.

        Returns a Contact object for a given contact id. Deleted contacts can
        still be retrieved but will be marked deleted and will not show up when
        searching for contacts.

        :path integer id: Id of contact
        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        """
        return self._get('/contacts/{id}'.format(id=id), query=query)

    def update_contact(self, id, body=None):
        """Update a contact.

        Update a contact.

        :path integer id: Id of contact
        :body body: contact
        :body -> Contact string workPhone: E.164 number
        :body -> Contact string mobilePhone: E.164 number
        :body -> Contact string firstName: First name of contact
        :body -> Contact boolean deleted: Return deleted contacts
        :body -> Contact string lastName: Last name of contact
        :body -> Contact string zipcode: ZIP code of contact
        :body -> Contact object properties: Map of string properties for
        contact
        :body -> Contact string externalId: External id of contact for syncing
        with external sources
        :body -> Contact string externalSystem: External system that external
        id refers to
        :body -> Contact integer id: Id of contact
        :body -> Contact string homePhone: E.164 number
        """
        return self._put('/contacts/{id}'.format(id=id), body=body)

    def get_contact_history(self, id, query=None):
        """Find a contact's history.

        Find all texts and calls attributed to a contact. Returns a list of
        calls and texts a contact has been involved with.

        :path integer id: Id of contact
        :query integer limit: Maximum number of records to return in a paged
        list response. The default is 100.
        :query integer offset: Offset to the start of a given page. The default
        is 0.
        """
        return self._get('/contacts/{id}/history'.format(id=id), query=query)

    def find_keywords(self, query=None):
        """Find keywords.

        Find keywords for purchase on the CallFire platform. If a keyword
        appears in the response, it is available for purchase. Repeat the
        "keywords" query parameter (at least one is required to see any data)
        for multiple searches in one request.

        :query array keywords: Keyword to search for
        """
        return self._get('/keywords', query=query)

    def find_keyword_leases(self, query=None):
        """Find keyword leases.

        Find all owned keyword leases for a user. A keyword lease is the
        ownership information involving a keyword.

        :query integer limit: Maximum number of records to return in a paged
        list response. The default is 100.
        :query integer offset: Offset to the start of a given page. The default
        is 0.
        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        """
        return self._get('/keywords/leases', query=query)

    def get_keyword_lease(self, keyword, query=None):
        """Find a specific lease.

        Returns a KeywordLease for a given keyword.

        :path string keyword: Keyword text that a lease is desired for
        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        """
        return self._get('/keywords/leases/{keyword}'.format(keyword=keyword),
                         query=query)

    def update_keyword_lease(self, keyword, body=None):
        """Update a lease.

        Update a keyword lease. Can only set autoRenew to false at this time.

        :path string keyword: Keyword to update lease for
        :body body: keywordLease
        :body -> KeywordLease string status: Lease status (PENDING, ACTIVE,
        RELEASED, UNAVAILABLE) *read only*
        :body -> KeywordLease integer leaseEnd: Lease end formatted in unix
        time *read only*
        :body -> KeywordLease string keyword: Text used as keyword
        :body -> KeywordLease integer leaseBegin: Lease begin formatted in unix
        time *read only*
        :body -> KeywordLease boolean autoRenew: Toggle auto renewal of keyword
        lease at end of each billing cycle
        :body -> KeywordLease string shortCode: Short code assigned to keyword
        """
        return self._put('/keywords/leases/{keyword}'.format(keyword=keyword),
                         body=body)

    def is_keyword_available(self, keyword):
        """Check for a specific keyword.

        Find an individual keyword for purchase on the CallFire platform.
        Returns boolean for availability.

        :path string keyword: Keyword to search for
        """
        return self._get(
            '/keywords/{keyword}/available'.format(keyword=keyword))

    def get_account(self):
        """Find account details.

        Find account details for the user. Details include name, email, and
        basic account permissions.

        """
        return self._get('/me/account')

    def find_api_credentials(self, query=None):
        """Find api credentials.

        Find all generated API credentials for the user. Returns a paged list
        of ApiCredential.

        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        :query integer limit: Maximum number of records to return in a paged
        list response. The default is 100.
        :query integer offset: Offset to the start of a given page. The default
        is 0.
        """
        return self._get('/me/api/credentials', query=query)

    def create_api_credential(self, body=None):
        """Create api credentials.

        Create API credentials for the CallFire API. This endpoint requires
        full CallFire account credentials to be used, authenticated using Basic
        Authentication. At this time, the user can only supply the name for the
        credentials. The generated credentials can be used to access any
        endpoint on the CallFire API.

        :body body: apiCredential
        :body -> ApiCredential string username: Username for credential
        :body -> ApiCredential string password: Password for credential
        :body -> ApiCredential boolean enabled: Is credential enabled
        :body -> ApiCredential integer id: Id of api credential
        :body -> ApiCredential string name: Name of api credential
        """
        return self._post('/me/api/credentials', body=body)

    def delete_api_credential(self, id):
        """Delete api credentials.

        Delete a specific API credential. Currently, removes the credentials
        ability to access the API.

        :path integer id: Id of api credential
        """
        return self._delete('/me/api/credentials/{id}'.format(id=id))

    def get_api_credential(self, id, query=None):
        """Find a specific api credential.

        Returns an ApiCredential instance for a given api credential id

        :path integer id: Id of api credential
        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        """
        return self._get('/me/api/credentials/{id}'.format(id=id), query=query)

    def get_billing_plan_usage(self):
        """Find plan usage.

        Find billing plan usage for the user. Returns billing plan usage for
        the current month.

        """
        return self._get('/me/billing/plan-usage')

    def get_caller_ids(self):
        """Find caller ids.

        Returns a list of verified caller ids. If the number is not shown in
        the list, then it is not verified, and will have to send for a
        verification code.

        """
        return self._get('/me/callerids')

    def send_verification_code_to_caller_id(self, callerid):
        """Create a caller id.

        Generates and sends a verification code to the phone number provided in
        the path. The verification code is delivered via a phone call. This
        code needs to be submitted to the verify caller id API endpoint.

        :path string callerid: E.164 number without the '+' that needs to be
        verified
        """
        return self._post('/me/callerids/{callerid}'.format(callerid=callerid))

    def verify_caller_id(self, callerid, body=None):
        """Verify a caller id.

        With the verification code received from the Create endpoint, a call to
        this endpoint is required to finish verification. An example would be
        with a code of 1234 post a body of {"verificationCode":1234} to this
        API.

        :path string callerid: E.164 number without the '+' that needs to be
        verified
        :body body: request
        :body -> CallerIdVerificationRequest string verificationCode: The code
        used to verify a caller id number
        """
        return self._post('/me/callerids/{callerid}/verification-code'.format(
            callerid=callerid), body=body)

    def create_media(self):
        """Create media.

        Create media for use in text messages

        """
        return self._post('/media')

    def get_media_data_by_key(self, key, extension):
        """Download media by extension.

        Download a media file of type (bmp, gif, jpg, m4a, mp3, mp4, png, wav)

        :path string key: ~
        :path string extension: ~
        """
        return self._get('/media/public/{key}.{extension}'.format(key=key,
                                                                  extension=extension))

    def get_media(self, id, query=None):
        """Get a specific media.

        Get media stored with text message

        :path integer id: ~
        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        """
        return self._get('/media/{id}'.format(id=id), query=query)

    def get_media_data(self, id, extension):
        """Download media by extension.

        Download a media file of type (bmp, gif, jpg, m4a, mp3, mp4, png, wav)

        :path integer id: ~
        :path string extension: ~
        """
        return self._get(
            '/media/{id}.{extension}'.format(id=id, extension=extension))

    def get_media_data_binary(self, id):
        """Download a MP3 media.

        Download a MP3 media

        :path integer id: ~
        """
        return self._get('/media/{id}/file'.format(id=id))

    def find_number_leases(self, query=None):
        """Find leases.

        Find all number leases for the user. This API is useful for finding all
        numbers currently owned by an account. Returns a paged list of
        NumberLease.

        :query integer limit: Maximum number of records to return in a paged
        list response. The default is 100.
        :query integer offset: Offset to the start of a given page. The default
        is 0.
        :query string prefix: 4-7 digit prefix
        :query string city: City name
        :query string state: State abbreviation code
        :query string zipcode: 5 digit zipcode
        :query string lata: Local access and transport area (LATA)
        :query string rateCenter: Rate center
        :query string labelName: Label name
        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        """
        return self._get('/numbers/leases', query=query)

    def find_number_lease_configs(self, query=None):
        """Find lease configs.

        Find all number lease configs for the user. Returns a paged list of
        NumberConfig.

        :query integer limit: Maximum number of records to return in a paged
        list response. The default is 100.
        :query integer offset: Offset to the start of a given page. The default
        is 0.
        :query string prefix: 4-7 digit prefix
        :query string city: City name
        :query string state: State name
        :query string zipcode: 5 digit zipcode
        :query string lata: Local access and transport area (LATA)
        :query string rateCenter: Rate center
        :query string labelName: Label name
        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        """
        return self._get('/numbers/leases/configs', query=query)

    def get_number_lease_config(self, number, query=None):
        """Find a specific lease config.

        Returns a single NumberConfig instance for a given number lease.

        :path string number: E.164 number sans +
        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        """
        return self._get(
            '/numbers/leases/configs/{number}'.format(number=number),
            query=query)

    def update_number_lease_config(self, number, body=None):
        """Update a lease config.

        Update a number lease config. Use this API endpoint to add an Inbound
        IVR or Call Tracking feature to a CallFire phone number.

        :path string number: E.164 number sans +
        :body body: numberConfig
        :body -> NumberConfig string configType: Type of config (TRACKING, IVR)
        :body -> NumberConfig callTrackingConfig: CallTrackingConfig object
        :body -> NumberConfig string number: E.164 number
        :body -> NumberConfig ivrInboundConfig: IvrInboundConfig object
        """
        return self._put(
            '/numbers/leases/configs/{number}'.format(number=number),
            body=body)

    def get_number_lease(self, number, query=None):
        """Find a specific lease.

        Returns a single NumberLease instance for a given number lease.

        :path string number: E.164 number sans +
        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        """
        return self._get('/numbers/leases/{number}'.format(number=number),
                         query=query)

    def update_number_lease(self, number, body=None):
        """Update a lease.

        Update a number lease instance. Ability to turn off autoRenew and
        toggle call/text features for a particular number.

        :path string number: E.164 number sans +
        :body body: numberLease
        :body -> NumberLease string status: Lease status (PENDING, ACTIVE,
        RELEASED, UNAVAILABLE) *read only*
        :body -> NumberLease integer leaseEnd: Lease end formatted in unix time
        *read only*
        :body -> NumberLease array labels: ~
        :body -> NumberLease string callFeatureStatus: Status of call feature
        :body -> NumberLease string nationalFormat: Formatted number with
        country code
        :body -> NumberLease region: Region object
        :body -> NumberLease integer leaseBegin: Lease begin formatted in unix
        time *read only*
        :body -> NumberLease string number: E.164 number
        :body -> NumberLease string textFeatureStatus: Status of text feature
        :body -> NumberLease boolean autoRenew: Toggle auto renewal of keyword
        lease at end of each billing cycle
        :body -> NumberLease boolean tollFree: Is number toll-free
        """
        return self._put('/numbers/leases/{number}'.format(number=number),
                         body=body)

    def find_numbers_local(self, query=None):
        """Find local numbers.

        Find numbers in the CallFire local numbers catalog that are available
        for purchase. At least one additional parameter is required.

        :query integer limit: Maximum number of records to return in a paged
        list response. The default is 100.
        :query string prefix: 4-7 digit prefix
        :query string city: City name
        :query string state: State name
        :query string zipcode: 5 digit zipcode
        :query string lata: Local access and transport area (LATA)
        :query string rateCenter: Rate center
        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        """
        return self._get('/numbers/local', query=query)

    def find_number_regions(self, query=None):
        """Find number regions.

        Find number region information. Use this API to obtain detailed region
        information that can then be used to query for more specific phone
        numbers than a general query.

        :query integer limit: Maximum number of records to return in a paged
        list response. The default is 100.
        :query integer offset: Offset to the start of a given page. The default
        is 0.
        :query string prefix: 4-7 digit prefix
        :query string city: City name
        :query string state: State name
        :query string zipcode: 5 digit zipcode
        :query string lata: Local access and transport area (LATA)
        :query string rateCenter: Rate center
        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        """
        return self._get('/numbers/regions', query=query)

    def find_numbers_tollfree(self, query=None):
        """Find tollfree numbers.

        Find numbers in the CallFire tollfree numbers catalog that are
        available for purchase.

        :query integer limit: Maximum number of records to return in a paged
        list response. The default is 100.
        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        """
        return self._get('/numbers/tollfree', query=query)

    def order_keywords(self, body=None):
        """Purchase keywords.

        Purchase keywords. Send a list of available keywords into this API to
        purchase them using CallFire credits. Be sure the account has credits
        before trying to purchase.

        :body body: request
        :body -> KeywordPurchaseRequest array keywords: List of keywords
        """
        return self._post('/orders/keywords', body=body)

    def order_numbers(self, body=None):
        """Purchase numbers.

        Purchase numbers. There are many ways to purchase a number. Set either
        tollFreeCount or localCount along with some querying fields to purchase
        numbers by bulk query. Set the list of numbers to purchase by list.
        Available numbers will be purchased using CallFire credits owned by the
        user. Be sure the account has credits before trying to purchase.

        :body body: request
        :body -> NumberPurchaseRequest string city: City of requested numbers
        :body -> NumberPurchaseRequest integer localCount: Total count of local
        numbers requested
        :body -> NumberPurchaseRequest integer tollFreeCount: Total count of
        toll-free numbers requested
        :body -> NumberPurchaseRequest string state: State of requested numbers
        :body -> NumberPurchaseRequest string zipcode: ZIP code of requested
        numbers
        :body -> NumberPurchaseRequest string prefix: Country prefix of
        requested numbers
        :body -> NumberPurchaseRequest string lata: Local access and transport
        area of requested numbers
        :body -> NumberPurchaseRequest array numbers: List of E.164 numbers
        :body -> NumberPurchaseRequest string rateCenter: Rate center of
        requested numbers
        """
        return self._post('/orders/numbers', body=body)

    def get_order(self, id, query=None):
        """Find a specific order.

        Returns a single NumberOrder instance for a given order id.

        :path integer id: Id of order
        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        """
        return self._get('/orders/{id}'.format(id=id), query=query)

    def find_texts(self, query=None):
        """Find texts.

        Finds all texts sent or received by the user. Use "id=0" for the
        campaignId parameter to query for all texts sent through the POST
        /texts API. See [call states and
        results](https://developers.callfire.com/results-responses-errors.html)

        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        :query integer limit: Maximum number of records to return in a paged
        list response. The default is 100.
        :query integer offset: Offset to the start of a given page. The default
        is 0.
        :query array id: List of text ids to query for
        :query integer campaignId: Query for texts inside of a particular
        campaign.
        :query integer batchId: ~
        :query string fromNumber: E.164 number that text was from
        :query string toNumber: E.164 number that text was sent to
        :query string label: Label of the text message
        :query string states: Expected text statuses in comma seperated string
        (READY, SELECTED, CALLBACK, FINISHED, DISABLED, DNC, DUP, INVALID,
        TIMEOUT, PERIOD_LIMIT)
        :query string results: Expected text results in comma seperated string
        (SENT, RECEIVED, DNT, TOO_BIG, INTERNAL_ERROR, CARRIER_ERROR,
        CARRIER_TEMP_ERROR, UNDIALED)
        :query boolean inbound: Specify true if inbounds, false if outbounds.
        Do not specify for both.
        :query integer intervalBegin: Start of the find interval in Unix time
        milliseconds
        :query integer intervalEnd: End of the find interval in Unix time
        milliseconds
        """
        return self._get('/texts', query=query)

    def send_texts(self, query=None, body=None):
        """Send texts.

        Use the /texts API to quickly send individual texts. A verified Caller
        ID and sufficient credits are required to make a call.

        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        :query integer campaignId: Specify a campaignId to send calls quickly
        on a previously created campaign
        :query string defaultMessage: ~
        :body body: textRecipients
        :body -> TextRecipient object attributes: Map of string attributes
        associated with recipient
        :body -> TextRecipient integer contactId: Id of contact
        :body -> TextRecipient string phoneNumber: E.164 number
        :body -> TextRecipient string message: Text message
        :body -> TextRecipient array media: ~
        """
        return self._post('/texts', query=query, body=body)

    def find_text_auto_replys(self, query=None):
        """Find auto replies.

        Find all text autoreplies created by the user. Returns a paged list of
        TextAutoReply.

        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        :query integer limit: Maximum number of records to return in a paged
        list response. The default is 100.
        :query integer offset: Offset to the start of a given page. The default
        is 0.
        :query string number: E.164 number that contains a TextAutoReply
        """
        return self._get('/texts/auto-replys', query=query)

    def create_text_auto_reply(self, body=None):
        """Create an auto reply.

        Auto-replies are text message replies sent to a customer when a
        customer replies to a text message from a campaign. A keyword will need
        to have been purchased before an Auto-Reply can be created.

        :body body: textAutoReply
        :body -> TextAutoReply string message: Message to return as auto reply
        :body -> TextAutoReply string match: Case insensitive text to match, if
        left empty will match all texts
        :body -> TextAutoReply integer id: Id of text auto reply
        :body -> TextAutoReply string keyword: Keyword for text auto reply
        :body -> TextAutoReply string number: E.164 number for text auto reply
        """
        return self._post('/texts/auto-replys', body=body)

    def delete_text_auto_reply(self, id):
        """Delete an auto reply.

        Deletes a text auto reply and removes the configuration. Can not delete
        a TextAutoReply currently active on a campaign.

        :path integer id: Id of text auto reply
        """
        return self._delete('/texts/auto-replys/{id}'.format(id=id))

    def get_text_auto_reply(self, id, query=None):
        """Find a specific auto reply.

        Returns a single TextAutoReply for a given text auto reply id

        :path integer id: Id of text auto reply
        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        """
        return self._get('/texts/auto-replys/{id}'.format(id=id), query=query)

    def find_text_broadcasts(self, query=None):
        """Find text broadcasts.

        Find all text broadcasts created by the user. Can query on label, name,
        and the current running status of the campaign. Returns a paged list of
        text broadcasts.

        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        :query integer limit: Maximum number of records to return in a paged
        list response. The default is 100.
        :query integer offset: Offset to the start of a given page. The default
        is 0.
        :query string label: Label of text broadcast
        :query string name: Name of text broadcast
        :query boolean running: Is broadcast running
        """
        return self._get('/texts/broadcasts', query=query)

    def create_text_broadcast(self, query=None, body=None):
        """Create a text broadcast.

        Create a text broadcast campaign using the Text Broadcast API. Send a
        TextBroadcast in the message body to detail a text broadcast campaign.
        A campaign can be created with no contacts and bare minimum
        configuration, but contacts will have to be added further on to use the
        campaign.

        :query boolean start: If true then start campaign immediately.
        :body body: textBroadcast
        :body -> TextBroadcast string status: Status of broadcast *read only*
        :body -> TextBroadcast string fromNumber: E.164 number or short code
        :body -> TextBroadcast array media: ~
        :body -> TextBroadcast string name: Name of broadcast
        :body -> TextBroadcast array recipients: List of TextRecipient objects
        :body -> TextBroadcast integer lastModified: DateTime formatted in unix
        time *read only*
        :body -> TextBroadcast array labels: Labels of broadcast
        :body -> TextBroadcast integer maxActive: Max number of active calls
        :body -> TextBroadcast string bigMessageStrategy: If message too big
        (SEND_MULTIPLE, DO_NOT_SEND, TRIM)
        :body -> TextBroadcast boolean resumeNextDay: ~
        :body -> TextBroadcast array schedules: ~
        :body -> TextBroadcast localTimeRestriction: LocalTimeRestriction
        object
        :body -> TextBroadcast string message: Text message
        :body -> TextBroadcast integer id: Id of broadcast
        :body -> TextBroadcast retryConfig: RetryConfig object
        """
        return self._post('/texts/broadcasts', query=query, body=body)

    def get_text_broadcast(self, id, query=None):
        """Find a specific text broadcast.

        Returns a single TextBroadcast instance for a given text broadcast id.

        :path integer id: Id of text broadcast
        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        """
        return self._get('/texts/broadcasts/{id}'.format(id=id), query=query)

    def update_text_broadcast(self, id, body=None):
        """Update a text broadcast.

        After having created a text broadcast campaign, this PUT lets the user
        modify the configuration of a text broadcast campaign. See
        TextBroadcast for more information on what can/can't be updated on this
        API.

        :path integer id: Id of text broadcast
        :body body: textBroadcast
        :body -> TextBroadcast string status: Status of broadcast *read only*
        :body -> TextBroadcast string fromNumber: E.164 number or short code
        :body -> TextBroadcast array media: ~
        :body -> TextBroadcast string name: Name of broadcast
        :body -> TextBroadcast array recipients: List of TextRecipient objects
        :body -> TextBroadcast integer lastModified: DateTime formatted in unix
        time *read only*
        :body -> TextBroadcast array labels: Labels of broadcast
        :body -> TextBroadcast integer maxActive: Max number of active calls
        :body -> TextBroadcast string bigMessageStrategy: If message too big
        (SEND_MULTIPLE, DO_NOT_SEND, TRIM)
        :body -> TextBroadcast boolean resumeNextDay: ~
        :body -> TextBroadcast array schedules: ~
        :body -> TextBroadcast localTimeRestriction: LocalTimeRestriction
        object
        :body -> TextBroadcast string message: Text message
        :body -> TextBroadcast integer id: Id of broadcast
        :body -> TextBroadcast retryConfig: RetryConfig object
        """
        return self._put('/texts/broadcasts/{id}'.format(id=id), body=body)

    def archive_text_broadcast(self, id):
        """Archive text broadcast.

        Archive a text broadcast

        :path integer id: Id of text broadcast to archive
        """
        return self._post('/texts/broadcasts/{id}/archive'.format(id=id))

    def get_text_broadcast_batches(self, id, query=None):
        """Find batches in a text broadcast.

        This endpoint will enable the user to page through all of the batches
        for a particular text broadcast campaign.

        :path integer id: Id of text broadcast
        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        :query integer limit: Maximum number of records to return in a paged
        list response. The default is 100.
        :query integer offset: Offset to the start of a given page. The default
        is 0.
        """
        return self._get('/texts/broadcasts/{id}/batches'.format(id=id),
                         query=query)

    def add_text_broadcast_batch(self, id, body=None):
        """Add batches to a text broadcast.

        The add batch API allows the user to add additional batches to an
        already created text broadcast campaign. The added batch will go
        through the CallFire validation process, unlike in the recipients
        version of this API. Because of this, use the scrubDuplicates flag to
        remove duplicates from your batch. Batches may be added as a contact
        list id, a list of contact ids, or a list of numbers.

        :path integer id: Id of text broadcast
        :body body: request
        :body -> BatchRequest boolean scrubDuplicates: Remove duplicate
        recipients in batch
        :body -> BatchRequest array recipients: List of Recipient objects
        :body -> BatchRequest string name: Name of batch
        :body -> BatchRequest integer contactListId: Id of contact list
        """
        return self._post('/texts/broadcasts/{id}/batches'.format(id=id),
                          body=body)

    def add_text_broadcast_recipients(self, id, query=None, body=None):
        """Add recipients to a text broadcast.

        Use this API to add recipients to an already created text broadcast.
        Post a list of Recipient objects for them to be immediately added to
        the text broadcast campaign. These contacts do not go through
        validation process, and will be acted upon as they are added.
        Recipients may be added as a list of contact ids, or list of numbers.

        :path integer id: Id of text broadcast
        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        :body body: textRecipients
        :body -> TextRecipient object attributes: Map of string attributes
        associated with recipient
        :body -> TextRecipient integer contactId: Id of contact
        :body -> TextRecipient string phoneNumber: E.164 number
        :body -> TextRecipient string message: Text message
        :body -> TextRecipient array media: ~
        """
        return self._post('/texts/broadcasts/{id}/recipients'.format(id=id),
                          query=query, body=body)

    def start_text_broadcast(self, id):
        """Start text broadcast.

        Start a text broadcast

        :path integer id: Id of text broadcast to start
        """
        return self._post('/texts/broadcasts/{id}/start'.format(id=id))

    def get_text_broadcast_stats(self, id, query=None):
        """Get statistics on text broadcast.

        Return text broadcast statistics

        :path integer id: ~
        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        :query integer begin: ~
        :query integer end: ~
        """
        return self._get('/texts/broadcasts/{id}/stats'.format(id=id),
                         query=query)

    def stop_text_broadcast(self, id):
        """Stop text broadcast.

        Stop a text broadcast

        :path integer id: Id of text broadcast to stop
        """
        return self._post('/texts/broadcasts/{id}/stop'.format(id=id))

    def get_text_broadcast_texts(self, id, query=None):
        """Find texts in a text broadcast.

        This endpoint will enable the user to page through all of the texts for
        a particular text broadcast campaign.

        :path integer id: The id of text broadcast
        :query integer batchId: ~
        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        :query integer limit: Maximum number of records to return in a paged
        list response. The default is 100.
        :query integer offset: Offset to the start of a given page. The default
        is 0.
        """
        return self._get('/texts/broadcasts/{id}/texts'.format(id=id),
                         query=query)

    def get_text(self, id, query=None):
        """Find a specific text.

        Returns a single Text instance for a given text id

        :path integer id: The id of the text
        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        """
        return self._get('/texts/{id}'.format(id=id), query=query)

    def find_webhooks(self, query=None):
        """Find webhooks.

        Find all webhooks for the user. Search for webhooks on name, resource,
        event, callback URL, or whether they are enabled. Returns a paged list
        of Webhook.

        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        :query integer limit: Maximum number of records to return in a paged
        list response. The default is 100.
        :query integer offset: Offset to the start of a given page. The default
        is 0.
        :query string name: Name of webhook
        :query string resource: Name of resource
        :query string event: Name of event
        :query string callback: Callback URL
        :query boolean enabled: Is webhook enabled
        """
        return self._get('/webhooks', query=query)

    def create_webhook(self, body=None):
        """Create a webhook.

        Create a Webhook for notification in the CallFire system. Use the
        webhooks API to receive notifications of important CallFire events.
        Select the resource to listen to, and then choose the events for that
        resource to receive notifications on. When an event triggers, a POST
        will be made to the callback URL with a payload of notification
        information.

        :body body: webhook
        """
        return self._post('/webhooks', body=body)

    def find_webhook_resources(self, query=None):
        """Find webhook resources.

        Find webhook resources. Available resources include 'CccCampaign':
        ['started', 'stopped', 'finished'], 'CallBroadcast': ['started',
        'stopped', 'finished'], 'TextBroadcast': ['started', 'stopped',
        'finished'], 'OutboundCall': ['finished'], 'InboundCall': ['finished'],
        'OutboundText': ['finished'], 'InboundText': ['finished']

        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        """
        return self._get('/webhooks/resources', query=query)

    def get_webhook_resource(self, resource, query=None):
        """Find specific webhook resource.

        Returns a single WebhookResource instance for a given webhookResource
        name

        :path string resource: Name of webhook resource
        :query string fields: Limit fields returned. E.g. fields=id,name or
        fields=items(id,name)
        """
        return self._get(
            '/webhooks/resources/{resource}'.format(resource=resource),
            query=query)

    def delete_webhook(self, id):
        """Delete a webhook.

        Delete a webhook. Will be removed permenantly.

        :path integer id: Id of webhook.
        """
        return self._delete('/webhooks/{id}'.format(id=id))

    def update_webhook(self, id, body=None):
        """Update a webhook.

        Update the information in a currently existing webhook. Most fields are
        updateable.

        :path integer id: Id of webhook.
        :body body: webhook
        """
        return self._put('/webhooks/{id}'.format(id=id), body=body)
