"""Shared entry point: streamlit run streamlit_app.py."""
import streamlit as st
from app.organizational.dashboard import main as team_diagnostic
from app.tool1.dashboard import main as message_coach


def overview():
    st.set_page_config(page_title='CommsAlign',layout='wide')
    st.markdown("""<style>
    .stApp {background:#F5F7FB;color:#20334A;}
    .block-container {max-width:1120px;padding-top:4rem;padding-bottom:3rem;}
    .st-key-brand h1 {text-align:center;font-size:clamp(2.8rem,6vw,4.6rem);letter-spacing:-.055em;color:#17365D;padding-bottom:.4rem;}
    .ca-symbol {display:block;width:160px;height:108px;margin:0 auto .6rem;}
    .ca-eyebrow {text-align:center;text-transform:uppercase;letter-spacing:.18em;font-size:.75rem;font-weight:700;color:#47717D;margin-bottom:.3rem;}
    .st-key-overview-intro, .st-key-overview-intro [data-testid="stMarkdown"], .st-key-overview-intro [data-testid="stMarkdownContainer"] {width:100%;}
    .ca-intro {text-align:center;width:100%;max-width:none;margin:0 auto 2.6rem;color:#526174;font-size:1.12rem;line-height:1.7;}
    [class*="st-key-tool-card-"] {background:white;border:1px solid #DEE6EF;border-radius:22px;padding:1.8rem;box-shadow:0 12px 35px #17365D08;min-height:350px;}
    .st-key-tool-card-one {border-top:4px solid #2F75B5;}
    .st-key-tool-card-two {border-top:4px solid #2E8B8B;}
    [class*="st-key-tool-card-"] h2 {font-size:1.7rem;color:#17365D;letter-spacing:-.025em;}
    [class*="st-key-tool-card-"] p {line-height:1.65;}
    .ca-tag {color:#426A88;font-size:.76rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;}
    .ca-foot {text-align:center;color:#607086;font-size:.88rem;line-height:1.6;margin:2.2rem auto 0;max-width:760px;}
    </style>""",unsafe_allow_html=True)
    st.markdown('<img class="ca-symbol" alt="CommsAlign: two conversation bubbles with aligned message lines" src="data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%20160%20108%22%3E%3Cpath%20d%3D%22M24%2014H78Q90%2014%2090%2026V62Q90%2074%2078%2074H38L20%2088V74Q8%2074%208%2062V26Q8%2014%2024%2014Z%22%20fill%3D%22%232F75B5%22%2F%3E%3Cpath%20d%3D%22M82%2014H136Q152%2014%20152%2026V62Q152%2074%20140%2074V88L122%2074H82Q70%2074%2070%2062V26Q70%2014%2082%2014Z%22%20fill%3D%22%232E8B8B%22%20stroke%3D%22%23F5F7FB%22%20stroke-width%3D%224%22%2F%3E%3Cpath%20d%3D%22M28%2036H54M28%2050H54M98%2036H128M98%2050H128%22%20fill%3D%22none%22%20stroke%3D%22white%22%20stroke-width%3D%226%22%20stroke-linecap%3D%22round%22%2F%3E%3C%2Fsvg%3E">',unsafe_allow_html=True)
    st.markdown('<div class="ca-eyebrow">Workplace communication, with perspective</div>',unsafe_allow_html=True)
    with st.container(key='brand'):
        st.title('CommsAlign')
    with st.container(key='overview-intro'):
        st.markdown('<p class="ca-intro">Understand your team’s signals. Bring more clarity to your messages.<br>Two tools to support thoughtful workplace conversations.</p>',unsafe_allow_html=True)
    left,right=st.columns(2,gap='large')
    with left:
        with st.container(key='tool-card-one'):
            st.markdown('<div class="ca-tag">Tool 1 · Review a message</div>',unsafe_allow_html=True)
            st.header('Message Coach')
            st.write('Get structured feedback on a task instruction or performance feedback draft before you share it.')
            st.markdown('- Review your draft against a message-specific rubric.\n- Inspect the evidence behind each rating.\n- Download the review for your own revision.')
            st.caption('Live evaluation requires your GW Azure connection. Automated rewriting is not available yet.')
            if st.button('Open Message Coach',type='primary',use_container_width=True):
                st.switch_page(st.Page(message_coach,title='Tool 1 — Message Coach',url_path='message-coach'))
    with right:
        with st.container(key='tool-card-two'):
            st.markdown('<div class="ca-tag">Tool 2 · Explore team signals</div>',unsafe_allow_html=True)
            st.header('Team Diagnostic')
            st.write('Explore aggregate survey patterns and turn a selected signal into a structured team discussion.')
            st.markdown('- See relative strengths and areas to explore.\n- Review evidence and privacy limitations.\n- Capture learning and export a follow-up summary.')
            st.caption('Currently uses synthetic demonstration data. Small-group results are suppressed by the reporting rule.')
            if st.button('Open Team Diagnostic',use_container_width=True):
                st.switch_page(st.Page(team_diagnostic,title='Tool 2 — Team Diagnostic',url_path='team-diagnostic'))
    st.markdown('<p class="ca-foot">A starting point for discussion, not a diagnosis. Survey interpretations and message ratings remain provisional. Nothing is automatically sent between tools or to employees.</p>',unsafe_allow_html=True)


if __name__=='__main__':
    st.navigation([
        st.Page(overview,title='Overview',default=True),
        st.Page(team_diagnostic,title='Tool 2 — Team Diagnostic',url_path='team-diagnostic'),
        st.Page(message_coach,title='Tool 1 — Message Coach',url_path='message-coach'),
    ]).run()
