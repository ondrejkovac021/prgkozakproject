### Jak zapnout a vypnout fullscreen režim v tomto kódu:

#### Zapnutí fullscreen:
- Když není okno již v režimu fullscreen, funkce `enterFullscreen()` požádá prohlížeč, aby přepnul stránku do fullscreen režimu.
- Může se to stát, když uživatel stiskne klávesu **Space** nebo **E**, nebo pokud je detekována nečinnost uživatele (15 sekund neaktivnosti) - automaticky se aktivuje fullscreen.

#### Vypnutí fullscreen:
- Funkce `exitFullscreen()` vypne fullscreen režim, pokud je aktivní, když uživatel pohne myší nebo stiskne jakoukoliv jinou klávesu než **Space** nebo **E**.

Tento kód také sleduje neaktivitu (15 sekund) a přepne se do fullscreen režimu automaticky, pokud uživatel neprovádí žádnou akci.
