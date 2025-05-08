# 🧠 Validador de Nombre

Este es un mini proyecto de práctica en Python que valida si un nombre ingresado por el usuario cumple con dos condiciones básicas:

- Tiene al menos **dos palabras**
- Cada palabra **empieza con mayúscula**

---

## 💡 ¿Cómo funciona?

1. El programa solicita al usuario que escriba su nombre completo.
2. Verifica:
   - Que haya **dos o más palabras** usando `.split()`
   - Que cada palabra empiece con mayúscula usando `.istitle()`
3. Devuelve un mensaje indicando si el nombre es válido o no.

---

## 📌 Ejemplo de uso

```bash
Ingrese su nombre y apellido por favor:
Luis Sosa

✅ Nombre válido
