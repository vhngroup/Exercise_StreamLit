import streamlit as st
import random
import secrets

#random.seed(10)
estado =0
def go_To_Draw(participants, num_winners): #Validate List Number of participants and winner
    f=[]
    if num_winners > len(participants):
        return participants
    #random aleatory result mixed participants and select winners
    while len(f) <= num_winners-1: #Ajustamos el indice
        d = secrets.choice(participants) #Seleccionamos uno aleatorio
        #Validamos si el valor ya existe en el vector (evita valores repetidos en el caso de ser mas de un ganador)
        if d not in f: 
            f.append(d) #Agregamos el ganador
    #return random.sample(participants, num_winners) 
    if len(f) > 1:
        return random.sample(f, len(f)) #Agregamos mas Aleatoriedad sobre el secret aplicamos random
    else:
        return f

def main():
    st.title("App para sorteos")
    #Validate if var participants exist in session state if is not, create
    if 'participants' not in st.session_state:
        st.session_state.participants=[]
    
    if 'draw_realized' not in st.session_state:
        st.session_state.draw_realized=False

    def clean():
        if new_participant and new_participant not in st.session_state.participants:
            #add participant to list participants
            st.session_state.participants.append(new_participant)
            st.session_state.my_text = st.session_state.widget
            st.session_state.widget = ""
            

    st.header("Agregar participantes")
    new_participant = st.text_input("Nombre del participante", key='widget')

    st.button("Agregar Concursante", on_click=clean)
    #Validate if exist in list of participants
    if len(st.session_state.participants) > 0 and st.session_state.widget == "":
        st.success(f"Participante {new_participant} agregado correctamente")
    else:
        st.warning(f"Por favor ingese el nombre del concursante")
    if new_participant in st.session_state.participants:
            st.warning(f"El participante !{new_participant}¡ ya esta en la lista")

    def refresh():
        st.session_state.ListBox = index=0

    st.header("Eliminar participantes")
    participant_to_delete=st.selectbox("Seleccione el participante a eliminar", 
                                       st.session_state.participants, key="ListBox")
    
    if st.button("Eliminar participante"):
        st.session_state.participants.remove(participant_to_delete)
        st.success(f"El Participante {new_participant} Se a eliminado satisfactoriamente")

    st.header("Lista de Participantes")
    for i, participant in enumerate(st.session_state.participants, 1):
        st.write(f"{i}. {participant}")

    st.header("Realizar sorteo")
    num_participants = len(st.session_state.participants)
    if num_participants > 0:
        num_winners = st.number_input("Numero de ganadores",
                                      min_value=1,
                                      max_value=num_participants,
                                      value=min(1, num_participants))
        if st.button("Realizar Sorteo"):
            winners = go_To_Draw(st.session_state.participants, num_winners)
            st.success("Sorteo Realizado")
            st.header("Ganadores: ")
            for i, winner in enumerate(winners, 1):
                st.write(f"{i}. {winner}")
            st.session_state.sorteo_realizado = True
    else:
        st.warning("No hay participantes para realizar el sorteo.")
    
    if st.button("Reiniciar Sorteo"):
        st.session_state.sorteo_realizado = False
        st.success("Todo Listo, puedes realizar un nuevo sorteo")
    
    if st.button("Eliminar todo los participantes"):
        st.session_state.participants =[]
        st.session_state.sorteo_realizado = False
        st.success("Todos los participantes han sido eliminados")


if __name__=="__main__":
    main() #Execute script with main function
