import argparse, json, time, sys
from pathlib import Path
from .core import scan
from .ui.logo import show_logo
from .ui.hero import wave_banner, info_panel, ScanSpinner

# ANSI color codes
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    # Background colors
    BG_RED = '\033[101m'
    BG_GREEN = '\033[102m'
    BG_YELLOW = '\033[103m'
    BG_BLUE = '\033[104m'
    BG_PURPLE = '\033[105m'
    BG_CYAN = '\033[106m'


def main():
    version = "0.1.0"
    shown = show_logo(version)
    if not shown:
        wave_banner(version, seconds=1.0)
    info_panel()
    
    # Enhanced URL input with validation
    print("\n🌐 Enter the website URL to scan:")
    url = input("URL: ").strip()
    
    if not url:
        print("❌ No URL provided. Exiting...")
        return
    
    # Add protocol if missing
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
        print(f"ℹ️  Added HTTPS protocol: {url}")
    
    print(f"\n🔍 Scanning: {url}")
    print("ℹ️  Initializing accessibility scanner...")
    
    try:
        with ScanSpinner("scanning…"):
            data = scan(url, None)
        
        violations = data.get('violations', [])
        
        # Enhanced results display
        if violations:
            print(f"⚠️  Found {len(violations)} accessibility violations")
            print(f"\n📋 VIOLATIONS FOUND:")
            print("=" * 60)
            
            for i, violation in enumerate(violations, 1):
                impact_color = Colors.RED if violation['impact'] == 'serious' else Colors.YELLOW if violation['impact'] == 'moderate' else Colors.BLUE
                impact_icon = "🔴" if violation['impact'] == 'serious' else "🟡" if violation['impact'] == 'moderate' else "🔵"
                
                print(f"\n{impact_icon} {i}. {violation['id']} ({impact_color}{violation['impact']} impact{Colors.END})")
                print(f"   📝 {violation['description']}")
                print(f"   🔧 {violation['help']}")
                if violation.get('helpUrl'):
                    print(f"   🔗 {violation['helpUrl']}")
        else:
            print("✅ No accessibility violations found! Great job!")
        
        # Enhanced save functionality
        print(f"\n💾 Save results to file? (y/n): ", end='')
        save_choice = input().strip().lower()
        if save_choice in ['y', 'yes']:
            print(f"📁 Enter filename (default: violations.json): ", end='')
            filename = input().strip()
            if not filename:
                filename = "violations.json"
            if not filename.endswith('.json'):
                filename += '.json'
            
            with open(filename, 'w') as f:
                json.dump(violations, f, indent=2)
            print(f"✅ Results saved to {filename}")
        
        print(f"\n🎉 Thank you for using A11Y-SCOUT! Keep building accessible web experiences!")
        
    except Exception as e:
        print(f"❌ Error scanning website: {e}")
        print("⚠️  Make sure the URL is accessible and try again")
        return
if __name__ == "__main__":
    main()
