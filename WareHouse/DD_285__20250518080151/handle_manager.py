'''
Contains the logic for managing handle changes.
'''
from input_validator import InputValidator  # Import the InputValidator
class HandleManager:
    def canChangeHandles(self, N: int, S: list, T: list) -> bool:
        # Validate input using InputValidator
        if not InputValidator.validate_input(N, S, T):
            return False
        used_handles = set(S)  # Set to track currently used handles
        handle_map = {S[i]: i for i in range(N)}  # Map current handles to their indices
        changes = []  # List to track changes that need to be processed
        for i in range(N):
            if S[i] == T[i]:
                continue  # Skip if current handle is the same as desired handle
            if T[i] not in used_handles:
                # If T[i] is not in use, change S[i] to T[i]
                used_handles.remove(S[i])
                used_handles.add(T[i])
                handle_map[T[i]] = i  # Update the handle map
            else:
                # T[i] is in use, record the change
                changes.append((S[i], T[i]))
        # Process the changes to ensure all can be fulfilled
        for current_handle, desired_handle in changes:
            if desired_handle in used_handles:
                # Find a user who can be reassigned to free up desired_handle
                found = False
                for j in range(N):
                    if S[j] != desired_handle and T[j] != desired_handle and S[j] not in used_handles:
                        # Free up the desired_handle
                        used_handles.remove(desired_handle)  # Remove the current user of desired_handle
                        used_handles.add(S[j])  # Change to a new handle
                        used_handles.add(desired_handle)  # Now desired_handle is in use
                        handle_map[S[j]] = handle_map[desired_handle]  # Update the handle map
                        S[handle_map[desired_handle]] = S[j]  # Update the current handle list
                        found = True
                        break
                if not found:
                    return False  # No valid handle found to free up desired_handle
            else:
                # If desired_handle is not in use, simply change it
                used_handles.remove(current_handle)
                used_handles.add(desired_handle)
        return True