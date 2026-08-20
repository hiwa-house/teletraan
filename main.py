import yaml
from markupsafe import Markup

def define_env(env):
    BADGE_CONFIG = {
        # Ratings
        'winnah': {'label': 'Winnah', 'class': 'badge-winnah', 'icon': '⭐'},
        'untested': {'label': 'Untested', 'class': 'badge-untested', 'icon': '❓'},
        'solid': {'label': 'Solid', 'class': 'badge-solid', 'icon': '📍'},
        # Service
        'dine-in': {'label': 'Dine In', 'class': 'badge-service', 'icon': '🍽️'},
        'counter': {'label': 'Counter', 'class': 'badge-service', 'icon': '🥡'},
        'activity': {'label': 'Activity', 'class': 'badge-service', 'icon': '🏄🏻'},
        # Types
        'bakery': {'label': 'Bakery', 'class': 'badge-type', 'icon': '🥐'},
        'brewery': {'label': 'Brewery', 'class': 'badge-type', 'icon': '🍺'},
        'bottle-shop': {'label': 'Bottle Shop', 'class': 'badge-type', 'icon': '🍷'},
        'pau-hana': {'label': 'Pau Hana', 'class': 'badge-type', 'icon': '🍹'},
        'frozen-treats': {'label': 'Frozen Treats', 'class': 'badge-type', 'icon': '🍧'},
        'grocery': {'label': 'Grocery', 'class': 'badge-type', 'icon': '🛒'},
        'day-date': {'label': 'Day Date', 'class': 'badge-type', 'icon': '💕'},
        '21-plus': {'label': '21+', 'class': 'badge-type', 'icon': '🔞'},
    }

    @env.macro
    def parse_yaml(data_str):
        return yaml.safe_load(data_str) if isinstance(data_str, str) else data_str

    @env.macro
    def render_filter_bar(places):
        if isinstance(places, str):
            places = yaml.safe_load(places)
        if not places:
            return ""
        
        all_tags = set()
        for place in places:
            if 'rating' in place: all_tags.add(place['rating'])
            if 'service' in place: all_tags.add(place['service'])
            for t in place.get('type', []): all_tags.add(t)

        html = ['<div class="city-guide-container">']
        html.append('<div class="filter-chip-bar"><span class="filter-label">Filter:</span>')
        html.append('<button class="chip active" data-filter="all">All</button>')
        for tag in sorted(all_tags):
            cfg = BADGE_CONFIG.get(tag, {'label': tag.replace('-', ' ').title(), 'icon': ''})
            html.append(f'<button class="chip" data-filter="{tag}">{cfg.get("icon", "")} {cfg["label"]}</button>')
        html.append('</div></div>')
        return Markup('\n'.join(html))

    @env.macro
    def render_places(places, neighborhood=None):
        if isinstance(places, str):
            places = yaml.safe_load(places)
        if not places:
            return ""

        if neighborhood:
            places = [p for p in places if p.get('neighborhood') == neighborhood]

        html = ['<ul class="place-list">']
        for p in places:
            tags = [p.get('rating'), p.get('service')] + p.get('type', [])
            tags_str = ' '.join(filter(None, tags))
            
            name_html = f'<a href="{p["url"]}" target="_blank" class="place-name">{p["name"]}</a>' if p.get('url') else f'<span class="place-name">{p["name"]}</span>'
            map_html = f'<a href="{p["map_url"]}" target="_blank" class="map-link" title="Directions">🧭</a>' if p.get('map_url') else ''
            
            badges_html = []
            for t in tags:
                if t in BADGE_CONFIG:
                    c = BADGE_CONFIG[t]
                    badges_html.append(f'<span class="badge {c["class"]}">{c["icon"]} {c["label"]}</span>')

            notes_html = f'''
            <details class="compact-notes">
                <summary><span class="note-toggle-icon">▸</span> Note</summary>
                <p>{p["notes"]}</p>
            </details>
            ''' if p.get('notes') else ''

            html.append(f'''
            <li class="place-item" data-tags="{tags_str}">
                <div class="place-row">
                    <div class="place-main"><span class="place-bullet">|</span> {name_html} {map_html}</div>
                    <div class="badge-group">{"".join(badges_html)}</div>
                </div>
                {notes_html}
            </li>
            ''')
        html.append('</ul>')
        
        return Markup('\n'.join(html))