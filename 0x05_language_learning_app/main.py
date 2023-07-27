# Import required modules
import React from 'react';
import { View, Text } from 'react-native';
import { createStackNavigator } from '@react-navigation/stack';
import { NavigationContainer } from '@react-navigation/native';
import LessonsScreen from './lessons_screen.py';
import QuizzesScreen from './quizzes_screen.py';

# Create a Stack Navigator
Stack = createStackNavigator();

# Main App Component
function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Lessons">
        <Stack.Screen name="Lessons" component={LessonsScreen} />
        <Stack.Screen name="Quizzes" component={QuizzesScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

# Start the app
if __name__ == "__main__":
    App()

