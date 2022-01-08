useEffect(
  () => {
    // hier wird etwas in der Mounting-Phase einmal ausgeführt
    return () => {
      // hier wird etwas nach der Unmounting-Phase einmal ausgeführt
    };
  },
  [] // keine Abhängigkeiten, bedeutet einmalige Ausführung
);