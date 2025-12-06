from rest_framework import serializers
from todo.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    datecompleted = serializers.ReadOnlyField()
    
    class Meta:
        model = Todo
        fields = ['id', 'title', 'created', 'datecompleted', 'important']


class TodoCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'datecompleted']   # allow updating datecompleted
        read_only_fields = ['id', 'title', 'created', 'important']
        
#Line 1 — Class definition: Defines a serializer named TodoSerializer that inherits from serializers.ModelSerializer.
# This tells DRF to auto-generate fields based on your Todo model and handle converting model instances ↔ JSON with built-in validation.

#Line 2 — created field (read-only): Adds a created field to the serializer but marks it as read-only. Clients will see this timestamp in responses, but they cannot set or change it in POST/PUT/PATCH.
# It reflects the value Django sets automatically with auto_now_add=True.

#Line 3 — datecompleted field (read-only): Adds datecompleted as read-only.
# It’s included in responses but blocked from client writes, ensuring only your backend logic (e.g., a “complete” endpoint) sets it to the current time. This prevents users from faking completion dates.

#Important note: Any field not explicitly marked read-only will be writable (if included in fields in Meta). Marking these two as read-only protects system-managed timestamps and keeps your data consistent and honest.