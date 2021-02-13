import clases

persona = clases.Persona()
persona.setNombre("Marcos")
persona.setApellidos("Astudillo")
persona.setAltura("174 cm")
persona.setEdad("35 años")

print(f"La persona es: {persona.getNombre()} {persona.getApellidos()}")
print(persona.hablar())

print("-------------------------")
informatico = clases.Informatico()
informatico.setNombre("Lucia")
informatico.setApellidos("Astudillo")


print(f"El informatico es: {informatico.getNombre()} {informatico.getApellidos()}")
print(f"Se los siguientes lenguajes informaticos {str(informatico.getLenguajes())}")
print(f"Mi experiencia es de: {informatico.experiencia}")
print("-------------------------")

tecnico = clases.TecnicoRedes()
tecnico.setNombre("Paulina")
print(tecnico.getNombre(),tecnico.auditarRedes,tecnico.getLenguajes())