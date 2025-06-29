'''
Module to manage user handles and handle change logic.
'''
class UserHandleManager:
    def __init__(self):
        self.current_handles = []
        self.desired_handles = []
        self.used_handles = set()
        self.change_order = []
    def add_user(self, current_handle, desired_handle):
        self.current_handles.append(current_handle)
        self.desired_handles.append(desired_handle)
    def process_handles(self):
        for i in range(len(self.current_handles)):
            current_handle = self.current_handles[i]
            desired_handle = self.desired_handles[i]
            if desired_handle not in self.used_handles:
                # If desired handle is not in use, proceed with the change
                self.used_handles.add(current_handle)
                self.used_handles.add(desired_handle)
                self.change_order.append((current_handle, desired_handle))
                self.current_handles[i] = desired_handle  # Update current handle
            else:
                # Find a temporary handle to free up the desired handle
                temp_handle_found = False
                for j in range(len(self.current_handles)):
                    if (self.current_handles[j] not in self.used_handles and 
                        self.current_handles[j] != current_handle):
                        # Temporarily change this handle
                        temp_handle = self.current_handles[j]
                        self.used_handles.remove(temp_handle)  # Free the temp handle
                        self.current_handles[j] = desired_handle  # Change to desired handle
                        self.used_handles.add(desired_handle)  # Add desired handle to used
                        self.change_order.append((temp_handle, desired_handle))  # Log the change
                        self.current_handles[i] = desired_handle  # Update the current handle for the original user
                        self.used_handles.add(current_handle)  # Add the original handle back to used
                        temp_handle_found = True
                        break
                # If no temporary handle was found, return an error
                if not temp_handle_found:
                    return "Error: Cannot fulfill handle change requests."
        return self.change_order