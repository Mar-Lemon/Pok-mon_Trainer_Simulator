class Pokemon:
    # Variable de clase para llevar el conteo total de Pokemon creados
    _contador_pokemons = 0

    def __init__(self, nombre: str, tipo: str, ataque: int, defensa: int, salud: int, nivel: int = 1):
        # Atributos de instancia (utilizando self)
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel
        self.ataque = ataque
        self.defensa = defensa
        self.salud = salud
        
        # Incrementamos el contador global de la clase
        Pokemon._contador_pokemons += 1
        print(f"Un nuevo {self.nombre} de tipo {self.tipo} ha sido capturado.")

    def __del__(self):
        # Destructor: Se ejecuta cuando el objeto es eliminado o liberado
        Pokemon._contador_pokemons = max(0, Pokemon._contador_pokemons - 1)
        print(f"{self.nombre} ha sido liberado y regreso a la naturaleza.")

    def mostrar_info(self):
        """Muestra los datos actuales del Pokemon."""
        print(f"\n=================================")
        print(f" STATS DE POKEMON")
        print(f"=================================")
        print(f" Nombre:  {self.nombre}")
        print(f" Tipo:    {self.tipo}")
        print(f" Nivel:   {self.nivel}")
        print(f" Ataque:  {self.ataque}")
        print(f" Defensa: {self.defensa}")
        print(f" Salud:   {self.salud}")
        print(f"=================================")

    def entrenar(self, *args):
        """
        Sobrecarga de metodos usando *args.
        - Si no recibe argumentos, mejora todas las estadisticas por defecto.
        - Si recibe argumentos (ej. 'ataque', 'defensa', 'salud'), mejora selectivamente.
        """
        self.nivel += 1
        
        if not args:
            self.ataque += 5
            self.defensa += 5
            self.salud += 10
            print(f"{self.nombre} entreno con intensidad y subio al Nivel {self.nivel}. Todas sus stats mejoraron.")
        else:
            mejoras = [arg.lower() for arg in args]
            if "ataque" in mejoras:
                self.ataque += 8
            if "defensa" in mejoras:
                self.defensa += 8
            if "salud" in mejoras:
                self.salud += 15
            print(f"Entrenamiento especializado para {self.nombre}. Nivel alcanzado: {self.nivel}.")

    def atacar(self, objetivo):
        """Simula un ataque a otro objeto Pokemon (Paso de parametros por referencia)."""
        print(f"\n{self.nombre} ataca a {objetivo.nombre}.")
        dano = max(1, self.ataque - (objetivo.defensa // 2))
        objetivo.salud -= dano
        if objetivo.salud < 0:
            objetivo.salud = 0
        print(f"{objetivo.nombre} recibio {dano} de dano. Salud restante: {objetivo.salud}")

    @classmethod
    def total_pokemons(cls):
        """Metodo de clase para consultar cuantos Pokemon existen en total."""
        return cls._contador_pokemons


def mostrar_menu():
    print("\n=================================")
    print("      SIMULADOR DE ENTRENADOR")
    print("=================================")
    print("1. Capturar nuevo Pokemon")
    print("2. Entrenar Pokemon")
    print("3. Ver informacion de todos los Pokemon")
    print("4. Calcular cuantos Pokemon existen")
    print("5. Liberar un Pokemon")
    print("6. Simular batalla entre Pokemon")
    print("7. Salir")
    print("=================================")


def main():
    # Lista para registrar los Pokemon capturados
    mis_pokemons = []

    while True:
        mostrar_menu()
        opcion = input("Elige una opcion (1-7): ").strip()

        if opcion == "1":
            print("\n--- CAPTURAR UN NUEVO POKEMON ---")
            nombre = input("Nombre del Pokemon: ").strip()
            tipo = input("Tipo (ej. Fuego, Agua, Electrico): ").strip()
            try:
                ataque = int(input("Puntos de Ataque (ej. 50): "))
                defensa = int(input("Puntos de Defensa (ej. 30): "))
                salud = int(input("Puntos de Salud (ej. 100): "))
                
                # Creacion de la instancia
                nuevo_pokemon = Pokemon(nombre, tipo, ataque, defensa, salud)
                mis_pokemons.append(nuevo_pokemon)
            except ValueError:
                print("Error: Ingresa valores numericos validos para las estadisticas.")

        elif opcion == "2":
            if not mis_pokemons:
                print("No tienes Pokemon registrados en tu equipo todavia.")
                continue
            
            print("\n--- ENTRENAR POKEMON ---")
            for i, poke in enumerate(mis_pokemons):
                print(f"{i + 1}. {poke.nombre} (Nivel {poke.nivel})")
            
            try:
                idx = int(input("Selecciona el numero del Pokemon a entrenar: ")) - 1
                if 0 <= idx < len(mis_pokemons):
                    pokemon_activo = mis_pokemons[idx]
                    
                    print("\nTipos de entrenamiento:")
                    print("1. Entrenamiento General (Todas las stats)")
                    print("2. Entrenamiento Especifico (Elige que mejorar)")
                    tipo_entreno = input("Elige una opcion (1 o 2): ").strip()
                    
                    if tipo_entreno == "2":
                        print("Escribe las estadisticas a mejorar separadas por espacio (ej. ataque salud):")
                        args_input = input("Stats: ").split()
                        pokemon_activo.entrenar(*args_input)
                    else:
                        pokemon_activo.entrenar()
                else:
                    print("Seleccion invalida.")
            except ValueError:
                print("Ingresa un numero valido.")

        elif opcion == "3":
            if not mis_pokemons:
                print("No hay Pokemon en tu lista.")
            else:
                for poke in mis_pokemons:
                    poke.mostrar_info()

        elif opcion == "4":
            total = Pokemon.total_pokemons()
            print(f"\nTotal de Pokemon registrados globalmente: {total}")

        elif opcion == "5":
            if not mis_pokemons:
                print("No hay Pokemon para liberar.")
                continue
            
            print("\n--- LIBERAR UN POKEMON ---")
            for i, poke in enumerate(mis_pokemons):
                print(f"{i + 1}. {poke.nombre} ({poke.tipo})")
            
            try:
                idx = int(input("Selecciona el numero del Pokemon que deseas liberar: ")) - 1
                if 0 <= idx < len(mis_pokemons):
                    liberado = mis_pokemons.pop(idx)
                    del liberado
                else:
                    print("Seleccion invalida.")
            except ValueError:
                print("Ingresa un numero valido.")

        elif opcion == "6":
            if len(mis_pokemons) < 2:
                print("Necesitas al menos 2 Pokemon para simular un combate.")
                continue
            
            print("\n--- SIMULACION DE COMBATE ---")
            for i, poke in enumerate(mis_pokemons):
                print(f"{i + 1}. {poke.nombre} (Salud: {poke.salud})")
            
            try:
                atacante_idx = int(input("Elige el numero del Pokemon atacante: ")) - 1
                defensor_idx = int(input("Elige el numero del Pokemon defensor: ")) - 1
                
                if 0 <= atacante_idx < len(mis_pokemons) and 0 <= defensor_idx < len(mis_pokemons):
                    if atacante_idx == defensor_idx:
                        print("Un Pokemon no puede atacarse a si mismo.")
                    else:
                        mis_pokemons[atacante_idx].atacar(mis_pokemons[defensor_idx])
                else:
                    print("Indices invalidos.")
            except ValueError:
                print("Ingresa numeros validos.")

        elif opcion == "7":
            print("\nGracias por jugar. Conviertete en un Maestro Pokemon.")
            break
        else:
            print("Opcion no valida. Por favor elige del 1 al 7.")


if __name__ == "__main__":
    main()