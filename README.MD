# 🌡️ Monitoreo Térmico con Activación de Ventilación  
Proyecto de Lenguaje de Programación Visual (LPV) – 2025
##👥Integrantes
- Lucas Gauto 
- Maurizio Valdez
- Fede Moreno 
- Juan Ibarra 
## 📌 Contexto
Este proyecto forma parte del **Trabajo Práctico de LPV**, desarrollado dentro del caso de estudio **"GreenTech Tower"**, un edificio corporativo que busca optimizar el consumo energético, mejorar la seguridad y garantizar el confort ambiental mediante la automatización con sensores y actuadores.

Nuestro grupo trabajó en el **módulo Nº 1: Lectura de Temperatura en oficinas y salas técnicas**, con el objetivo de **monitorear las condiciones térmicas** y **activar ventilación automática** cuando se superen los umbrales establecidos.

---

## 🎯 Objetivos
- Medir en tiempo real la temperatura ambiente en diferentes salas.  
- Visualizar datos en una interfaz gráfica amigable.  
- Activar ventiladores automáticamente al detectar temperaturas elevadas.  
- Registrar datos para análisis y toma de decisiones.  

---

## ⚙️ Tecnologías Utilizadas
- **Microcontroladores**: Arduino / ESP32  
- **Lenguajes**:  
  - C++ (Arduino) para la lógica de sensores y actuadores.  
  - Python (Tkinter / PyQt) para la interfaz gráfica.  
- **Sensores**: DS18B20 (temperatura).  
- **Actuadores**: Ventiladores.  
- **Comunicación**: Serial y/o WiFi.  
- **Base de datos**: SQLite o MySQL para registro histórico.  

---

## 🖥️ Funcionamiento
1. El **sensor DS18B20** mide la temperatura en oficinas y salas técnicas.  
2. El microcontrolador procesa los valores y los envía a la PC/servidor.  
3. La **interfaz gráfica en Python** muestra en tiempo real la temperatura medida.  
4. Si la temperatura supera el umbral configurado, se activa el **ventilador** automáticamente.  
5. Los datos se guardan en la base de datos para consultas posteriores.  

---



