import pygame

# Funkcja do rysowania konturu linii
def draw_line_outline(screen, start_x, start_y, end_x, end_y, color, thickness=1):
    """
    Rysuje linię między dwoma punktami.

    screen - ekran Pygame.
    start_x, start_y - współrzędne początku linii.
    end_x, end_y - współrzędne końca linii.
    color - kolor linii (RGB).
    thickness - grubość linii (domyślnie 1).
    """
    pygame.draw.line(screen, color, (start_x, start_y), (end_x, end_y), thickness)


# Funkcja do rysowania konturu okręgu
def draw_circle_outline(screen, center_x, center_y, radius, color, thickness=1):
    """
    Rysuje okrąg na ekranie (tylko kontur).

    screen - ekran Pygame.
    center_x, center_y - współrzędne środka okręgu.
    radius - promień okręgu.
    color - kolor okręgu (RGB).
    thickness - grubość obramowania okręgu.
    """
    pygame.draw.circle(screen, color, (center_x, center_y), radius, thickness)


# Funkcja do rysowania konturu prostokąta
def draw_rectangle_outline(screen, x, y, width, height, color, thickness=1):
    """
    Rysuje prostokąt na ekranie (tylko kontur).

    screen - ekran Pygame.
    x, y - współrzędne lewego górnego rogu prostokąta.
    width, height - szerokość i wysokość prostokąta.
    color - kolor prostokąta (RGB).
    thickness - grubość obramowania prostokąta.
    """
    pygame.draw.rect(screen, color, (x, y, width, height), thickness)


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Rysowanie konturów")

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))  # Wypełnienie białym kolorem

        # Przykładowe rysowanie konturów
        draw_line_outline(screen, 50, 50, 200, 50, (255, 0, 0), thickness=5)  # Czerwona linia
        draw_circle_outline(screen, 400, 300, 50, (0, 255, 0), thickness=5)  # Zielony okrąg kontur
        draw_rectangle_outline(screen, 500, 100, 150, 100, (0, 0, 255), thickness=3)  # Niebieski prostokąt kontur

        pygame.display.flip()

    pygame.quit()

import pygame
import random

# Funkcja do inicjalizacji ekranu
def init_screen(width, height, title="Gra"):
    """
    Inicjalizuje ekran o zadanej szerokości i wysokości.
    """
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(title)
    return screen


# Funkcja do wypełnienia ekranu kolorem
def fill_screen(screen, color):
    """
    Wypełnia ekran zadanym kolorem.
    """
    screen.fill(color)
    pygame.display.flip()


# Funkcja do rysowania kwadratu o zadanym rozmiarze i kolorze
def draw_rectangle(screen, x, y, width, height, color):
    """
    Rysuje prostokąt na ekranie.
    x, y - współrzędne lewego górnego rogu kwadratu.
    width, height - szerokość i wysokość prostokąta.
    color - kolor kwadratu.
    """
    pygame.draw.rect(screen, color, (x, y, width, height))


# Funkcja do rysowania koła o zadanym rozmiarze i kolorze
def draw_circle(screen, x, y, radius, color):
    """
    Rysuje koło na ekranie.
    x, y - współrzędne środka koła.
    radius - promień koła.
    color - kolor koła.
    """
    pygame.draw.circle(screen, color, (x, y), radius)


# Funkcja do losowania wartości kroku lub przesunięcia
def random_step(min_val, max_val):
    """
    Losuje wartość kroku lub przesunięcia z zakresu [min_val, max_val].
    """
    return random.randint(min_val, max_val)


# Funkcja do odczytywania kliknięcia myszką
def get_mouse_click():
    """
    Zwraca współrzędne kliknięcia myszką, jeśli nastąpiło.
    """
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            return event.pos  # Zwraca (x, y)
    return None


# Funkcja do rysowania pliku graficznego na zadanej pozycji
def draw_image(screen, image_path, x, y, width, height):
    """
    Rysuje obrazek na ekranie.
    image_path - ścieżka do pliku graficznego.
    x, y - współrzędne lewego górnego rogu obrazka.
    width, height - docelowe wymiary obrazka (skaluje).
    """
    try:
        image = pygame.image.load(image_path)
        image = pygame.transform.scale(image, (width, height))
        screen.blit(image, (x, y))
    except pygame.error as e:
        print(f"Nie udało się załadować obrazka: {e}")

# Funkcja do odczytywania kliknięcia myszką
def get_mouse_click():
    """
    Zwraca współrzędne kliknięcia myszką, jeśli nastąpiło.
    """
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            return event.pos  # Zwraca (x, y)
        elif event.type == pygame.QUIT:
            pygame.quit()
            exit()
    return None


# Przykład użycia komponentów
if __name__ == "__main__":
    # Parametry ekranu
    screen_width, screen_height = 800, 600
    screen = init_screen(screen_width, screen_height, "Komponenty Pygame")

    fill_screen(screen, (255, 255, 255))  # Wypełnienie białym kolorem

    # Przykładowe rysowanie
    draw_rectangle(screen,200,200,200,300,'red')  # Czerwony kwadrat
    draw_circle(screen, 400, 300, 50, (0, 0, 255))  # Niebieskie koło
    draw_image(screen, "icon.png", 500, 200, 100, 100)  # Ikonka
    pygame.display.flip()

    running = True
    while running:
        # Wywołanie funkcji do obsługi kliknięcia myszką
        mouse_click = get_mouse_click()
        if mouse_click:  # Jeśli kliknięto myszką
            print("Kliknięto myszką na współrzędnych:", mouse_click)
